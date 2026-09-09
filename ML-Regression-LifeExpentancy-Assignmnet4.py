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

df = pd.read_csv("Life_Expentancy_Data.csv")
df.columns = df.columns.str.strip()

df = df.dropna(subset=["Life expectancy"])

df = df.drop(columns=["Country"])

#EDA 
print("Shape:", df.shape)
print(df.head())
print(df.describe().round(2))
print("Missing values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

#GRAPH of Life Expentancy 
plt.figure(figsize=(7, 5))
plt.hist(df["Life expectancy"], bins=40)
plt.title("Distribution of Life Expectancy")
plt.xlabel("Life Expectancy")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

#Correlation Heatmap 
plt.figure(figsize=(12, 9))
sns.heatmap(df.select_dtypes(include=np.number).corr(), annot=False, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

#School and Income Graph 
plt.figure(figsize=(7, 5))
plt.scatter(df["Schooling"], df["Life expectancy"], alpha=0.3)
plt.xlabel("Schooling (years)")
plt.ylabel("Life Expectancy")
plt.title("Schooling vs Life Expectancy")
plt.tight_layout()
plt.show()

#Adult Mortality & Life Expentancy Graph
plt.figure(figsize=(7, 5))
plt.scatter(df["Adult Mortality"], df["Life expectancy"], alpha=0.3)
plt.xlabel("Adult Mortality")
plt.ylabel("Life Expectancy")
plt.title("Adult Mortality vs Life Expectancy")
plt.tight_layout()
plt.show()

#MISSING VALEUS 
target = "Life expectancy"
X = df.drop(columns=[target])
y = df[target]

#Enconding Values 
categorical_features = ["Status"]
numeric_features = [c for c in X.columns if c not in categorical_features]

#Scale Numerical Values 
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

#TRAIN TEST SPLIT 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training Data:", X_train.shape)
print("Testing Data:", X_test.shape)

#BASELINE MODELS + COMPARE MULTIPLE ALGORITHMS 
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree Regressor": DecisionTreeRegressor(max_depth=8, min_samples_leaf=4, random_state=42),
    "Random Forest Regressor": RandomForestRegressor(
        n_estimators=300, max_depth=15, min_samples_leaf=2, random_state=42, n_jobs=-1
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
final_pred = final_model.predict(X_test)

plt.figure(figsize=(7, 6))
plt.scatter(y_test, final_pred, alpha=0.4)
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color="red", linewidth=2
)
plt.xlabel("Actual Life Expectancy")
plt.ylabel("Predicted Life Expectancy")
plt.title(f"Actual vs Predicted Life Expectancy ({best_model_name})")
plt.tight_layout()
plt.show()