import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, HistGradientBoostingRegressor

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

#LOAD DATA
df = pd.read_csv("housing.csv")

print("Shape:", df.shape)
print(df.info())
print("Missing values:\n", df.isnull().sum())

#EDA

plt.figure(figsize=(7, 5))
plt.hist(df["median_house_value"], bins=50)
plt.title("Distribution of Median House Value")
plt.xlabel("Median House Value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

numeric_df = df.select_dtypes(include=np.number)
correlation = numeric_df.corr()

plt.figure(figsize=(9, 7))
plt.imshow(correlation, cmap="coolwarm")
plt.colorbar()
plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=90)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 5))
plt.scatter(df["median_income"], df["median_house_value"], alpha=0.2)
plt.xlabel("Median Income")
plt.ylabel("Median House Value")
plt.title("Median Income vs House Value")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 6))
plt.scatter(df["longitude"], df["latitude"], c=df["median_house_value"],
            cmap="viridis", alpha=0.4, s=10)
plt.colorbar(label="House Value")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("House Value by Location")
plt.tight_layout()
plt.show()

#DATA CLEANING

df = df[df["median_house_value"] < 500001].copy()

target = "median_house_value"
X = df.drop(columns=[target])
y = np.log1p(df[target])

#FEATURE ENGINEERING

X["rooms_per_household"] = X["total_rooms"] / X["households"]
X["bedrooms_per_room"] = X["total_bedrooms"] / X["total_rooms"]
X["population_per_household"] = X["population"] / X["households"]
X = X.replace([np.inf, -np.inf], np.nan)

#TRAIN TEST SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#PREPROCESSING

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

#MODELS TO COMPARE

models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(max_depth=12, min_samples_leaf=4, random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=250, max_depth=20, min_samples_leaf=2,
                                            random_state=42, n_jobs=-1),
    "HistGradientBoosting": HistGradientBoostingRegressor(max_depth=8, learning_rate=0.05,
                                                            max_iter=500, random_state=42)
}

results = []
fitted_pipelines = {}

for name, regressor in models.items():

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("regressor", regressor)
    ])

    pipeline.fit(X_train, y_train)
    fitted_pipelines[name] = pipeline

    pred_log = pipeline.predict(X_test)
    y_test_real = np.expm1(y_test)
    pred_real = np.expm1(pred_log)

    mae = mean_absolute_error(y_test_real, pred_real)
    rmse = np.sqrt(mean_squared_error(y_test_real, pred_real))
    r2 = r2_score(y_test_real, pred_real)

    results.append({"Model": name, "MAE": mae, "RMSE": rmse, "R2": r2})

    print(f"\n{name}")
    print("MAE :", round(mae, 2))
    print("RMSE:", round(rmse, 2))
    print("R2  :", round(r2, 4))

#MODEL COMPARISON

comparison = pd.DataFrame(results).sort_values("RMSE")

print("\n" + "=" * 50)
print("MODEL COMPARISON (sorted by RMSE)")
print("=" * 50)
print(comparison.round(2))

#PICK BEST MODEL

best_model_name = comparison.iloc[0]["Model"]
final_model = fitted_pipelines[best_model_name]

print("\nBest Model:", best_model_name)

cv_scores = cross_val_score(final_model, X_train, y_train, cv=5, scoring="r2", n_jobs=-1)
print("Mean CV R2 of Best Model:", round(cv_scores.mean(), 4))

#ACTUAL VS PREDICTED

final_pred_log = final_model.predict(X_test)
y_test_real = np.expm1(y_test)
final_pred_real = np.expm1(final_pred_log)

plt.figure(figsize=(7, 6))
plt.scatter(y_test_real, final_pred_real, alpha=0.3)
plt.plot(
    [y_test_real.min(), y_test_real.max()],
    [y_test_real.min(), y_test_real.max()],
    color="red", linewidth=2
)
plt.xlabel("Actual House Value")
plt.ylabel("Predicted House Value")
plt.title(f"Actual vs Predicted ({best_model_name})")
plt.tight_layout()
plt.show()
