import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score,
    f1_score,
    balanced_accuracy_score
)

#LOAD DATA

train_df = pd.read_csv("trainloan.csv")
test_df = pd.read_csv("testloan.csv")

print("Train Shape:", train_df.shape)
print("Test Shape:", test_df.shape)

print("\nTarget Distribution:")
print(train_df["Loan_Status"].value_counts())
print(train_df["Loan_Status"].value_counts(normalize=True))

#BASIC EDA

print("\nMissing Values:")
print(train_df.isnull().sum())

print("\nDuplicate Rows:", train_df.duplicated().sum())

#FEATURES AND TARGET

X = train_df.drop(columns=["Loan_Status", "Loan_ID"])
y = train_df["Loan_Status"]

test_ids = test_df["Loan_ID"]
X_test = test_df.drop(columns=["Loan_ID"])

#FEATURE ENGINEERING

def feature_engineering(df):

    df = df.copy()

    # Convert Dependents
    df["Dependents_Number"] = (
        df["Dependents"]
        .replace("3+", 3)
        .astype(float)
    )

    # Total income
    df["Total_Income"] = (
        df["ApplicantIncome"] +
        df["CoapplicantIncome"]
    )

    # Income per dependent
    df["Income_Per_Dependent"] = (
        df["Total_Income"] /
        (df["Dependents_Number"] + 1)
    )

    # Loan amount / income
    df["Loan_Income_Ratio"] = (
        df["LoanAmount"] /
        (df["Total_Income"] + 1)
    )

    # Income / loan
    df["Income_Loan_Ratio"] = (
        df["Total_Income"] /
        (df["LoanAmount"] + 1)
    )

    # Applicant contribution
    df["Applicant_Income_Ratio"] = (
        df["ApplicantIncome"] /
        (df["Total_Income"] + 1)
    )

    # Coapplicant contribution
    df["Coapplicant_Income_Ratio"] = (
        df["CoapplicantIncome"] /
        (df["Total_Income"] + 1)
    )

    # Log transformations
    df["Log_Total_Income"] = np.log1p(df["Total_Income"])
    df["Log_ApplicantIncome"] = np.log1p(df["ApplicantIncome"])
    df["Log_LoanAmount"] = np.log1p(df["LoanAmount"])

    return df


X = feature_engineering(X)
X_test = feature_engineering(X_test)

#IDENTIFY COLUMNS

numeric_features = X.select_dtypes(
    include=["int64", "float64"]
).columns.tolist()

categorical_features = X.select_dtypes(
    include=["object","string"]
).columns.tolist()

print("\nNumerical Features:")
print(numeric_features)

print("\nCategorical Features:")
print(categorical_features)

#PREPROCESSING

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

#TRAIN/VALIDATION SPLIT

X_train, X_val, y_train, y_val = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTrain Split:", X_train.shape)
print("Validation Split:", X_val.shape)

#CROSS VALIDATION

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

#MODELS AND HYPERPARAMETERS 

models = {

    "Logistic Regression": {

        "model": LogisticRegression(
            max_iter=2000
        ),

        "params": {
            "model__C": [0.01, 0.1, 1, 10, 50],
            "model__class_weight": [
                None,
                "balanced"
            ]
        }
    },


    "Decision Tree": {

        "model": DecisionTreeClassifier(
            random_state=42
        ),

        "params": {
            "model__max_depth": [2, 3, 4, 5, 6, 8],
            "model__min_samples_split": [2, 5, 10, 20],
            "model__min_samples_leaf": [1, 2, 5, 10],
            "model__class_weight": [
                None,
                "balanced"
            ]
        }
    },


    "Random Forest": {

        "model": RandomForestClassifier(
            random_state=42
        ),

        "params": {
            "model__n_estimators": [200, 300],
            "model__max_depth": [3, 5, 7, 10],
            "model__min_samples_split": [2, 5, 10, 20],
            "model__min_samples_leaf": [1, 2, 5],
            "model__class_weight": [
                None,
                "balanced"
            ]
        }
    }
}


#TRAIN MODELS 

results = {}
trained_models = {}

for name, config in models.items():

    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", config["model"])
    ])

    grid_search = GridSearchCV(
        pipeline,
        config["params"],
        cv=cv,
        scoring="balanced_accuracy",
        n_jobs=-1
    )

    grid_search.fit(X_train, y_train)

    best_model = grid_search.best_estimator_

    trained_models[name] = best_model

    print("Best Parameters:")
    print(grid_search.best_params_)

    # Validation prediction
    y_pred = best_model.predict(X_val)

    print("\nClassification Report:")
    print(classification_report(y_val, y_pred))

    print("Confusion Matrix:")
    print(confusion_matrix(y_val, y_pred))

    results[name] = {
        "Accuracy": accuracy_score(y_val, y_pred),
        "Balanced Accuracy": balanced_accuracy_score(y_val, y_pred),
        "Macro F1": f1_score(y_val, y_pred, average="macro")
    }

#MODEL COMPARISON

results_df = pd.DataFrame(results).T

print("\n" + "=" * 60)
print("MODEL COMPARISON")
print("=" * 60)

print(results_df.sort_values(
    "Balanced Accuracy",
    ascending=False
))

#SELECT BEST MODEL 

best_model_name = results_df[
    "Balanced Accuracy"
].idxmax()

best_model = trained_models[best_model_name]

print("\nBest Model:", best_model_name)

#THRESHOLD TUNING

probabilities = best_model.predict_proba(X_val)

classes = best_model.classes_

y_probability = probabilities[
    :, list(classes).index("Y")
]

threshold_results = []

for threshold in np.arange(0.10, 0.61, 0.01):

    predictions = np.where(
        y_probability >= threshold,
        "Y",
        "N"
    )

    report = classification_report(
        y_val,
        predictions,
        output_dict=True
    )

    balanced_acc = balanced_accuracy_score(
        y_val,
        predictions
    )

    threshold_results.append({
        "Threshold": threshold,
        "N Recall": report["N"]["recall"],
        "Y Recall": report["Y"]["recall"],
        "N F1": report["N"]["f1-score"],
        "Y F1": report["Y"]["f1-score"],
        "Macro F1": report["macro avg"]["f1-score"],
        "Balanced Accuracy": balanced_acc
    })


threshold_df = pd.DataFrame(threshold_results)

best_threshold_row = threshold_df.loc[
    threshold_df["Balanced Accuracy"].idxmax()
]

best_threshold = best_threshold_row["Threshold"]

print("\nBest Threshold:", best_threshold)

print("\nThreshold Results:")
print(best_threshold_row)

#FINAL VALIDATION PREDICTION

final_val_pred = np.where(
    y_probability >= best_threshold,
    "Y",
    "N"
)

print("\n" + "=" * 60)
print("FINAL VALIDATION RESULTS")
print("=" * 60)

print(
    classification_report(
        y_val,
        final_val_pred
    )
)

print("Confusion Matrix:")
print(confusion_matrix(
    y_val,
    final_val_pred
))

print(
    "Balanced Accuracy:",
    balanced_accuracy_score(
        y_val,
        final_val_pred
    )
)

#TRAIN BEST MODEL ON FULL DATA 

best_model.fit(X, y)

#TEST PREDICTIONS

test_probabilities = best_model.predict_proba(X_test)

test_classes = best_model.classes_

test_y_probability = test_probabilities[
    :, list(test_classes).index("Y")
]

test_predictions = np.where(
    test_y_probability >= best_threshold,
    "Y",
    "N"
)

#CHECK PREDICTION DISTRIBUTION

print("\n" + "=" * 60)
print("TEST PREDICTION DISTRIBUTION")
print("=" * 60)

print(
    pd.Series(test_predictions).value_counts()
)

print(
    pd.Series(test_predictions)
    .value_counts(normalize=True)
)

#CREATE SUBMISSION FILE 

submission = pd.DataFrame({
    "Loan_ID": test_ids,
    "Loan_Status": test_predictions
})

submission.to_csv(
    "loan_predictions.csv",
    index=False
)

print("\nloan_predictions.csv created successfully!")

print("\nFirst 10 Predictions:")
print(submission.head(10))



