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

df = pd.read_csv("insurance.csv")

#EDA 
print("Shape:", df.shape)
print(df.head())
print(df.describe().round(2))
print("Missing values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

#Distribution of Charges 
plt.figure(figsize=(7, 5))
plt.hist(df["charges"], bins=50)
plt.title("Distribution of Insurance Charges")
plt.xlabel("Charges")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

#Correlation Heatmap 
plt.figure(figsize=(6, 5))
sns.heatmap(df.select_dtypes(include=np.number).corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

#GRAPH of Smoker and Charges 
plt.figure(figsize=(6, 5))
sns.boxplot(x="smoker", y="charges", data=df)
plt.title("Charges by Smoker Status")
plt.tight_layout()
plt.show()

#Age vs Charges 
plt.figure(figsize=(7, 5))
plt.scatter(df["age"], df["charges"], alpha=0.3)
plt.xlabel("Age")
plt.ylabel("Charges")
plt.title("Age vs Charges")
plt.tight_layout()
plt.show()

df = df.drop_duplicates()
print("Shape after removing duplicate:", df.shape)

target = "charges"
X = df.drop(columns=[target])
y = df[target]

#FEATURE ENGINEERING 
X["is_obese"] = (X["bmi"] >= 30).astype(int)

#ENCODE CATEGORICAL VALUES 
categorical_features = ["sex", "smoker", "region"]
numeric_features = [c for c in X.columns if c not in categorical_features]

#SCALE NUMERICAL FEATURES 
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

#BASELINE MODELS + COMPARE ALGORITHMS 
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree Regressor": DecisionTreeRegressor(max_depth=6, min_samples_leaf=5, random_state=42),
    "Random Forest Regressor": RandomForestRegressor(
        n_estimators=200, max_depth=6, min_samples_leaf=5, random_state=42, n_jobs=-1
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

#GRAPH OF ACTUAL VS PREDICTED 
final_pred = final_model.predict(X_test)

plt.figure(figsize=(7, 6))
plt.scatter(y_test, final_pred, alpha=0.4)
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color="red", linewidth=2
)
plt.xlabel("Actual Charges")
plt.ylabel("Predicted Charges")
plt.title(f"Actual vs Predicted Charges ({best_model_name})")
plt.tight_layout()
plt.show()