import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

#LOAD DATA 
df = pd.read_csv("Automobile_data.csv")

numeric_string_columns =["bore", "stroke", "horsepower", "peak-rpm", "price"]
for col in numeric_string_columns:
    df[col] = pd.to_numeric(df[col],errors="coerce")

#CLEAN DATA 
df = df.dropna(subset=["price"])

#REMOVE COLUMNS 
df = df.drop(columns=["symboling", "normalized-losses"])

#EDA
print("Shape:", df.shape)
print(df.head())
print(df.describe().round(2))
print("Missing values:\n", df.isnull().sum())

#Distribution of Price 
plt.figure(figsize=(7, 5))
plt.hist(df["price"], bins=30)
plt.title("Distribution of Car Price")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

#Correlation Heatmap 
plt.figure(figsize=(9, 7))
sns.heatmap(df.select_dtypes(include=np.number).corr(), annot=False, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

#Graph of Engine Size and Price 
plt.figure(figsize=(7, 5))
plt.scatter(df["engine-size"], df["price"], alpha=0.4)
plt.xlabel("Engine Size")
plt.ylabel("Price")
plt.title("Engine Size vs Price")
plt.tight_layout()
plt.show()

#FEATURES AND TARGET
target = "price"
X = df.drop(columns=[target])
y = np.log1p(df[target])   

#FEATURE ENGINEERING 
cylinder_map = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "eight": 8, "twelve": 12}
door_map = {"two": 2, "four": 4}

X["num-of-cylinders"] = X["num-of-cylinders"].map(cylinder_map)
X["num-of-doors"] = X["num-of-doors"].map(door_map)

#TRAIN TEST SPLIT 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training Data:", X_train.shape)
print("Testing Data:", X_test.shape)

#ENCODE + SCALE PIPELINE 
numeric_features = X.select_dtypes(include=np.number).columns.tolist()
categorical_features = [c for c in X.columns if c not in numeric_features]

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, numeric_features),
    ("cat", categorical_pipeline, categorical_features)
])

#MODELS 
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree Regressor": DecisionTreeRegressor(max_depth=5, min_samples_leaf=4, random_state=42),
    "Random Forest Regressor": RandomForestRegressor(
        n_estimators=200, max_depth=8, min_samples_leaf=3, random_state=42, n_jobs=-1
    )
}

results = []
fitted_pipelines = {}

for name, algorithm in models.items():

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("regressor", algorithm)
    ])

    pipeline.fit(X_train, y_train)
    fitted_pipelines[name] = pipeline

    pred_log = pipeline.predict(X_test)
    y_test_real = np.expm1(y_test)
    pred_real = np.expm1(pred_log)

    mae = mean_absolute_error(y_test_real, pred_real)
    rmse = np.sqrt(mean_squared_error(y_test_real, pred_real))
    r2 = r2_score(y_test_real, pred_real)

    cv_scores = cross_val_score(pipeline, X_train, y_train, cv=5, scoring="r2", n_jobs=-1)
    cv_r2 = cv_scores.mean()

    results.append({"Model": name, "MAE": mae, "RMSE": rmse, "Test_R2": r2, "CV_R2": cv_r2})

    print(f"\n{name}")
    print("MAE    :", round(mae, 2))
    print("RMSE   :", round(rmse, 2))
    print("Test R2:", round(r2, 4))
    print("CV R2  :", round(cv_r2, 4))

#MODEL COMPARISON 
comparison = pd.DataFrame(results).sort_values("CV_R2", ascending=False)

print("\n" + "=" * 50)
print("MODEL COMPARISON (sorted by CV R2)")
print("=" * 50)
print(comparison.round(2))

best_model_name = comparison.iloc[0]["Model"]
final_model = fitted_pipelines[best_model_name]

print("\nBest Model:", best_model_name)
print("Mean CV R2 of Best Model:", round(comparison.iloc[0]["CV_R2"], 4))

#FEATURES IMPORTANCE 
if hasattr(final_model.named_steps["regressor"], "feature_importances_"):
    feature_names = final_model.named_steps["preprocessor"].get_feature_names_out()
    importance = final_model.named_steps["regressor"].feature_importances_

    feature_importance = pd.DataFrame({
        "Feature": feature_names,
        "Importance": importance
    }).sort_values("Importance", ascending=False)

    print("\nTop 10 Important Features:")
    print(feature_importance.head(10).round(4))

#ACTUAL VS PREDICTED GRAPH 
final_pred_log = final_model.predict(X_test)
y_test_real = np.expm1(y_test)
final_pred = np.expm1(final_pred_log)

plt.figure(figsize=(7, 6))
plt.scatter(y_test_real, final_pred, alpha=0.5)
plt.plot(
    [y_test_real.min(), y_test_real.max()],
    [y_test_real.min(), y_test_real.max()],
    color="red", linewidth=2
)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title(f"Actual vs Predicted Price ({best_model_name})")
plt.tight_layout()
plt.show()