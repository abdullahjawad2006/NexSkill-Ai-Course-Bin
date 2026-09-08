import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    roc_auc_score
)

df = pd.read_csv("diagnosis.csv")

print("\n========== DATASET ==========")
print("Shape:", df.shape)
print(df.head())

#BASIC EDA 

print("\n========== DATA INFORMATION ==========")
df.info()

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATES ==========")
print("Duplicate rows:", df.duplicated().sum())

print("\n========== TARGET DISTRIBUTION ==========")
print(df["diagnosis"].value_counts())

#DATA CLEANING

if "id" in df.columns:
    df = df.drop(columns=["id"])

empty_columns = df.columns[df.isnull().all()]

if len(empty_columns) > 0:
    df = df.drop(columns=empty_columns)

print("\n========== AFTER CLEANING ==========")
print("Shape:", df.shape)

#FEATURE ENGINEERING

X = df.drop(columns=["diagnosis"])

y = df["diagnosis"].map({
    "B": 0,
    "M": 1
})

print("\n========== FEATURES ==========")
print("Number of features:", X.shape[1])

#TRAIN/VALIDATION SPLIT

X_train, X_temp, y_train, y_temp = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp,
    y_temp,
    test_size=0.50,
    random_state=42,
    stratify=y_temp
)

print("\n========== DATA SPLIT ==========")

print("Training data  :", X_train.shape)
print("Validation data:", X_val.shape)
print("Testing data   :", X_test.shape)

#BASELINE MODEL

baseline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),

    ("scaler", StandardScaler()),

    ("model", LogisticRegression(
        max_iter=5000
    ))
])

baseline.fit(X_train, y_train)

baseline_pred = baseline.predict(X_val)

print("\n========== BASELINE ==========")
print("Logistic Regression")

print("Accuracy :",
      round(accuracy_score(y_val, baseline_pred), 4))

print("Precision:",
      round(precision_score(y_val, baseline_pred), 4))

print("Recall   :",
      round(recall_score(y_val, baseline_pred), 4))

print("F1 Score :",
      round(f1_score(y_val, baseline_pred), 4))

#MODEL COMPARISON

models = {

    "Logistic Regression": Pipeline([
        ("imputer", SimpleImputer(strategy="median")),

        ("scaler", StandardScaler()),

        ("model", LogisticRegression(
            max_iter=5000
        ))
    ]),

    "Decision Tree": Pipeline([
        ("imputer", SimpleImputer(strategy="median")),

        ("model", DecisionTreeClassifier(
            random_state=42
        ))
    ]),

    "Random Forest": Pipeline([
        ("imputer", SimpleImputer(strategy="median")),

        ("model", RandomForestClassifier(
            random_state=42,
            n_jobs=-1
        ))
    ])
}


print("\n========== MODEL COMPARISON ==========")

results = []

for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_val)

    accuracy = accuracy_score(
        y_val,
        predictions
    )

    precision = precision_score(
        y_val,
        predictions,
        zero_division=0
    )

    recall = recall_score(
        y_val,
        predictions,
        zero_division=0
    )

    f1 = f1_score(
        y_val,
        predictions,
        zero_division=0
    )

    results.append([
        name,
        accuracy,
        precision,
        recall,
        f1
    ])

    print("\n", name)

    print("Accuracy :",
          round(accuracy, 4))

    print("Precision:",
          round(precision, 4))

    print("Recall   :",
          round(recall, 4))

    print("F1 Score :",
          round(f1, 4))

#CREATE COMPARISON TABLE 

results_df = pd.DataFrame(
    results,
    columns=[
        "Model",
        "Accuracy",
        "Precision",
        "Recall",
        "F1"
    ]
)

print("\n========== MODEL COMPARISON TABLE ==========")

print(
    results_df.sort_values(
        "F1",
        ascending=False
    ).to_string(index=False)
)

#HYPERPARAMETER TUNING 

print("\n========== RANDOM FOREST TUNING ==========")


rf_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),

    ("model", RandomForestClassifier(
        random_state=42,
        n_jobs=-1
    ))
])


param_grid = {

    "model__n_estimators": [
        200,
        300,
        500
    ],

    "model__max_depth": [
        None,
        5,
        10,
        15
    ],

    "model__min_samples_split": [
        2,
        5
    ],

    "model__min_samples_leaf": [
        1,
        2
    ],

    "model__class_weight": [
        None,
        "balanced"
    ]
}


grid_search = GridSearchCV(

    estimator=rf_pipeline,

    param_grid=param_grid,

    scoring="f1",

    cv=5,

    n_jobs=-1
)


grid_search.fit(
    X_train,
    y_train
)


best_model = grid_search.best_estimator_


print("\nBest Parameters:")
print(grid_search.best_params_)

print("\nBest Cross Validation F1:")
print(round(grid_search.best_score_, 4))

#VALIDATION EVALUATION

val_pred = best_model.predict(X_val)

print("\n========== TUNED RANDOM FOREST ==========")

print("Accuracy :",
      round(accuracy_score(y_val, val_pred), 4))

print("Precision:",
      round(precision_score(y_val, val_pred), 4))

print("Recall   :",
      round(recall_score(y_val, val_pred), 4))

print("F1 Score :",
      round(f1_score(y_val, val_pred), 4))

#VALIDATION THRESHOLD TUNING 

val_probabilities = best_model.predict_proba(
    X_val
)[:, 1]


threshold_results = []


for threshold in np.arange(
    0.30,
    0.71,
    0.01
):

    threshold_pred = (
        val_probabilities >= threshold
    ).astype(int)

    precision = precision_score(
        y_val,
        threshold_pred,
        zero_division=0
    )

    recall = recall_score(
        y_val,
        threshold_pred,
        zero_division=0
    )

    f1 = f1_score(
        y_val,
        threshold_pred,
        zero_division=0
    )

    threshold_results.append([
        threshold,
        precision,
        recall,
        f1
    ])


threshold_df = pd.DataFrame(

    threshold_results,

    columns=[
        "Threshold",
        "Precision",
        "Recall",
        "F1"
    ]
)


#SELECT THRESHOLD ON BEST F1 SCORE 

best_threshold_row = threshold_df.loc[
    threshold_df["F1"].idxmax()
]


best_threshold = best_threshold_row["Threshold"]


print("\n========== BEST THRESHOLD ==========")

print(
    "Threshold:",
    round(best_threshold, 2)
)

print(
    "Precision:",
    round(
        best_threshold_row["Precision"],
        4
    )
)

print(
    "Recall:",
    round(
        best_threshold_row["Recall"],
        4
    )
)

print(
    "F1 Score:",
    round(
        best_threshold_row["F1"],
        4
    )
)

#FINAL MODEL TUNING 

X_final_train = pd.concat([
    X_train,
    X_val
])

y_final_train = pd.concat([
    y_train,
    y_val
])


print("\n========== FINAL TRAINING ==========")

print(
    "Final training samples:",
    len(X_final_train)
)


best_model.fit(
    X_final_train,
    y_final_train
)

#FINAL TEST PREDICTION

test_probabilities = best_model.predict_proba(
    X_test
)[:, 1]


test_predictions = (
    test_probabilities >= best_threshold
).astype(int)

#FINAL TEST RESULTS 

accuracy = accuracy_score(
    y_test,
    test_predictions
)

precision = precision_score(
    y_test,
    test_predictions,
    zero_division=0
)

recall = recall_score(
    y_test,
    test_predictions,
    zero_division=0
)

f1 = f1_score(
    y_test,
    test_predictions,
    zero_division=0
)

roc_auc = roc_auc_score(
    y_test,
    test_probabilities
)


print("\n")
print("=" * 60)
print("              FINAL TEST RESULTS")
print("=" * 60)

print(
    "Accuracy :",
    round(accuracy, 4)
)

print(
    "Precision:",
    round(precision, 4)
)

print(
    "Recall   :",
    round(recall, 4)
)

print(
    "F1 Score :",
    round(f1, 4)
)

print(
    "ROC-AUC  :",
    round(roc_auc, 4)
)

#CONFUSION MATRIX 

cm = confusion_matrix(
    y_test,
    test_predictions
)


print("\n========== CONFUSION MATRIX ==========")

print(cm)

#CLASSIFICATION REPORT 

print("\n========== CLASSIFICATION REPORT ==========")

print(
    classification_report(
        y_test,
        test_predictions,
        target_names=[
            "Benign",
            "Malignant"
        ],
        zero_division=0
    )
)


print("\n========== PROJECT COMPLETE ==========")