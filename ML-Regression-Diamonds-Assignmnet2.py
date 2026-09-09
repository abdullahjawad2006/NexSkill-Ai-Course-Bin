import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.impute import SimpleImputer

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("diamonds.csv")

df = df.drop(columns=["Unnamed: 0"])   

#EDA 
print("Shape:", df.shape)
print(df.head())
print(df.describe().round(2))
print("Missing values:\n", df.isnull().sum())

#GRAPH of Distribution of Price 
plt.figure(figsize=(7, 5))
plt.hist(df["price"], bins=50)
plt.title("Distribution of Diamond Price")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

#CORRELATION HEATMAP
plt.figure(figsize=(8, 6))
sns.heatmap(df.select_dtypes(include=np.number).corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

#CARAT is strong predictor of diamond price 
plt.figure(figsize=(7, 5))
plt.scatter(df["carat"], df["price"], alpha=0.2)
plt.xlabel("Carat")
plt.ylabel("Price")
plt.title("Carat vs Price")
plt.tight_layout()
plt.show()

df = df[(df["x"] > 0) & (df["y"] > 0) & (df["z"] > 0)]

print("Shape after removing invalid rows:", df.shape)

#FEATURE ENGINEERING 
df["volume"] = df["x"] * df["y"] * df["z"]

target = "price"
X = df.drop(columns=[target])
y = df[target]

#ENCODING VALUES 
cut_order = ["Fair", "Good", "Very Good", "Premium", "Ideal"]
color_order = ["J", "I", "H", "G", "F", "E", "D"]
clarity_order = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]

categorical_features = ["cut", "color", "clarity"]
numeric_features = [c for c in X.columns if c not in categorical_features]

#SCALE NUMERICAL VALUES 
numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OrdinalEncoder(categories=[cut_order, color_order, clarity_order]))
])

preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, numeric_features),
    ("cat", categorical_pipeline, categorical_features)
])

#TRAIN TEST SPLIT 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training Data:", X_train.shape)
print("Testing Data:", X_test.shape)

#BASELINE MODELS + COMPARE ALGORITHMS 
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree Regressor": DecisionTreeRegressor(max_depth=12, min_samples_leaf=4, random_state=42),
    "Random Forest Regressor": RandomForestRegressor(
        n_estimators=200, max_depth=20, min_samples_leaf=2, random_state=42, n_jobs=-1
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

    y_pred = pipeline.predict(X_test)

    #EVALUATION METRICS 
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    results.append({"Model": name, "MAE": mae, "RMSE": rmse, "R2": r2})

    print(f"\n{name}")
    print("MAE :", round(mae, 2))
    print("RMSE:", round(rmse, 2))
    print("R2  :", round(r2, 4))

#COMPARISON TABLE 
comparison = pd.DataFrame(results).sort_values("RMSE")

print("\n" + "=" * 50)
print("MODEL COMPARISON (sorted by RMSE)")
print("=" * 50)
print(comparison.round(2))

#SELECT BEST MODEL 
best_model_name = comparison.iloc[0]["Model"]
final_model = fitted_pipelines[best_model_name]

print("\nBest Model:", best_model_name)

#CROSS VALIDATION 
cv_scores = cross_val_score(final_model, X_train, y_train, cv=5, scoring="r2", n_jobs=-1)
print("Mean CV R2 of Best Model:", round(cv_scores.mean(), 4))

#ACTUAL VS PREDICTED VALUE GRAPH 
final_pred = final_model.predict(X_test)

plt.figure(figsize=(7, 6))
plt.scatter(y_test, final_pred, alpha=0.3)
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color="red", linewidth=2
)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title(f"Actual vs Predicted Price ({best_model_name})")
plt.tight_layout()
plt.show()

