import pandas as pd

from sklearn.model_selection import train_test_split, GridSearchCV

from sklearn.pipeline import Pipeline

from sklearn.preprocessing import (
    StandardScaler,
    OneHotEncoder
)

from sklearn.compose import ColumnTransformer

from sklearn.impute import SimpleImputer

from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
    make_scorer
)


# ============================================================
# 1. LOAD DATASET
# ============================================================

df = pd.read_csv(
    "WA_Fn-UseC_-HR-Employee-Attrition.csv"
)


# ============================================================
# 2. BASIC DATA INSPECTION
# ============================================================

print("=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

print("Dataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nAttrition Distribution:")
print(df["Attrition"].value_counts())


# ============================================================
# 3. REMOVE DUPLICATE ROWS
# ============================================================

df = df.drop_duplicates().copy()


# ============================================================
# 4. REMOVE UNNECESSARY COLUMNS
# ============================================================

df = df.drop(
    columns=[
        "EmployeeNumber",
        "EmployeeCount",
        "Over18",
        "StandardHours"
    ]
)


# ============================================================
# 5. FEATURE ENGINEERING
# ============================================================

def feature_engineering(df):

    df = df.copy()

    # --------------------------------------------------------
    # Income based features
    # --------------------------------------------------------

    df["TotalIncome"] = (
        df["MonthlyIncome"] +
        df["DailyRate"] +
        df["HourlyRate"]
    )

    df["Income_Per_JobLevel"] = (
        df["MonthlyIncome"] /
        (df["JobLevel"] + 1)
    )

    # --------------------------------------------------------
    # Experience based features
    # --------------------------------------------------------

    df["Years_Per_Company"] = (
        df["YearsAtCompany"] /
        (df["TotalWorkingYears"] + 1)
    )

    df["Years_Per_Manager"] = (
        df["YearsWithCurrManager"] /
        (df["YearsAtCompany"] + 1)
    )

    df["Years_Per_Promotion"] = (
        df["YearsSinceLastPromotion"] /
        (df["YearsAtCompany"] + 1)
    )

    df["Age_Per_Experience"] = (
        df["Age"] /
        (df["TotalWorkingYears"] + 1)
    )

    # --------------------------------------------------------
    # Satisfaction features
    # --------------------------------------------------------

    df["Satisfaction_Score"] = (
        df["JobSatisfaction"] +
        df["EnvironmentSatisfaction"] +
        df["RelationshipSatisfaction"] +
        df["JobInvolvement"]
    )

    df["Job_Satisfaction_Interaction"] = (
        df["JobSatisfaction"] *
        df["JobInvolvement"]
    )

    df["Environment_Job_Satisfaction"] = (
        df["EnvironmentSatisfaction"] *
        df["JobSatisfaction"]
    )

    # --------------------------------------------------------
    # Overtime flag
    # --------------------------------------------------------

    df["OverTime_Flag"] = (
        df["OverTime"] == "Yes"
    ).astype(int)

    # --------------------------------------------------------
    # Job level and income interaction
    # --------------------------------------------------------

    df["JobLevel_Income"] = (
        df["JobLevel"] *
        df["MonthlyIncome"]
    )

    return df


df = feature_engineering(df)


# ============================================================
# 6. SEPARATE FEATURES AND TARGET
# ============================================================

X = df.drop(
    columns=["Attrition"]
)

y = df["Attrition"].map({
    "No": 0,
    "Yes": 1
})


# ============================================================
# 7. TRAIN / VALIDATION SPLIT
# ============================================================

X_train, X_valid, y_train, y_valid = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Rows:", X_train.shape[0])
print("Validation Rows:", X_valid.shape[0])


# ============================================================
# 8. NUMERICAL AND CATEGORICAL FEATURES
# ============================================================

numeric_features = X.select_dtypes(
    include=["int64", "float64"]
).columns

categorical_features = X.select_dtypes(
    include=["object", "str"]
).columns


print("\nNumber of Numerical Features:")
print(len(numeric_features))

print("\nNumber of Categorical Features:")
print(len(categorical_features))


# ============================================================
# 9. NUMERICAL PREPROCESSING
# ============================================================

numeric_pipeline = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(
                strategy="median"
            )
        ),

        (
            "scaler",
            StandardScaler()
        )
    ]
)


# ============================================================
# 10. CATEGORICAL PREPROCESSING
# ============================================================

categorical_pipeline = Pipeline(
    steps=[

        (
            "imputer",
            SimpleImputer(
                strategy="most_frequent"
            )
        ),

        (
            "encoder",
            OneHotEncoder(
                handle_unknown="ignore",
                sparse_output=False
            )
        )
    ]
)


# ============================================================
# 11. COMBINE PREPROCESSING
# ============================================================

preprocessor = ColumnTransformer(
    transformers=[

        (
            "num",
            numeric_pipeline,
            numeric_features
        ),

        (
            "cat",
            categorical_pipeline,
            categorical_features
        )
    ]
)


# ============================================================
# 12. F1 SCORER
# ============================================================

f1_scorer = make_scorer(
    f1_score,
    pos_label=1
)


# ============================================================
# 13. MODELS
# ============================================================

models = {

    "Logistic Regression": LogisticRegression(
        max_iter=3000,
        random_state=42
    ),

    "Decision Tree": DecisionTreeClassifier(
        random_state=42
    ),

    "Random Forest": RandomForestClassifier(
        random_state=42,
        n_jobs=-1
    )
}


# ============================================================
# 14. HYPERPARAMETER GRIDS
# ============================================================

param_grids = {


    # --------------------------------------------------------
    # LOGISTIC REGRESSION
    # --------------------------------------------------------

    "Logistic Regression": {

        "model__C": [
            0.01,
            0.1,
            0.5,
            1,
            2,
            5
        ],

        "model__class_weight": [
            None,
            "balanced",
            {0: 1, 1: 2},
            {0: 1, 1: 3}
        ]
    },


    # --------------------------------------------------------
    # DECISION TREE
    # --------------------------------------------------------

    "Decision Tree": {

        "model__max_depth": [
            3,
            4,
            5,
            6,
            8,
            10
        ],

        "model__min_samples_split": [
            2,
            5,
            10,
            20
        ],

        "model__min_samples_leaf": [
            1,
            2,
            4,
            8
        ],

        "model__class_weight": [
            None,
            "balanced",
            {0: 1, 1: 2},
            {0: 1, 1: 3}
        ]
    },


    # --------------------------------------------------------
    # RANDOM FOREST
    # --------------------------------------------------------

    "Random Forest": {

        "model__n_estimators": [
            200,
            400
        ],

        "model__max_depth": [
            4,
            6,
            8,
            10
        ],

        "model__min_samples_split": [
            2,
            5,
            10
        ],

        "model__min_samples_leaf": [
            1,
            2,
            4
        ],

        "model__class_weight": [
            None,
            "balanced",
            {0: 1, 1: 2},
            {0: 1, 1: 3}
        ]
    }
}


# ============================================================
# 15. TRAIN + GRID SEARCH
# ============================================================

results = []

best_models = {}


for model_name, model in models.items():

    print("\n")
    print("=" * 60)
    print("TRAINING:", model_name)
    print("=" * 60)


    pipeline = Pipeline(
        steps=[

            (
                "preprocessor",
                preprocessor
            ),

            (
                "model",
                model
            )
        ]
    )


    grid_search = GridSearchCV(

        estimator=pipeline,

        param_grid=param_grids[
            model_name
        ],

        scoring=f1_scorer,

        cv=5,

        n_jobs=-1,

        verbose=1
    )


    # --------------------------------------------------------
    # TRAIN
    # --------------------------------------------------------

    grid_search.fit(
        X_train,
        y_train
    )


    best_model = grid_search.best_estimator_

    best_models[
        model_name
    ] = best_model


    # --------------------------------------------------------
    # VALIDATION PREDICTION
    # --------------------------------------------------------

    y_pred = best_model.predict(
        X_valid
    )


    # --------------------------------------------------------
    # METRICS
    # --------------------------------------------------------

    accuracy = accuracy_score(
        y_valid,
        y_pred
    )

    precision = precision_score(
        y_valid,
        y_pred,
        zero_division=0
    )

    recall = recall_score(
        y_valid,
        y_pred,
        zero_division=0
    )

    f1 = f1_score(
        y_valid,
        y_pred,
        zero_division=0
    )


    # --------------------------------------------------------
    # SAVE RESULTS
    # --------------------------------------------------------

    results.append({

        "Model": model_name,

        "Accuracy": accuracy,

        "Precision": precision,

        "Recall": recall,

        "F1 Score": f1
    })


    # --------------------------------------------------------
    # PRINT BEST PARAMETERS
    # --------------------------------------------------------

    print("\nBest Parameters:")

    print(
        grid_search.best_params_
    )


    print("\nBest Cross Validation F1:")

    print(
        round(
            grid_search.best_score_,
            4
        )
    )


    # --------------------------------------------------------
    # PRINT VALIDATION RESULTS
    # --------------------------------------------------------

    print("\nValidation Accuracy:")
    print(
        round(
            accuracy,
            4
        )
    )

    print("\nValidation Precision:")
    print(
        round(
            precision,
            4
        )
    )

    print("\nValidation Recall:")
    print(
        round(
            recall,
            4
        )
    )

    print("\nValidation F1:")
    print(
        round(
            f1,
            4
        )
    )


    # --------------------------------------------------------
    # CLASSIFICATION REPORT
    # --------------------------------------------------------

    print("\nClassification Report:")

    print(
        classification_report(
            y_valid,
            y_pred,
            target_names=[
                "No Attrition",
                "Attrition"
            ],
            zero_division=0
        )
    )


    # --------------------------------------------------------
    # CONFUSION MATRIX
    # --------------------------------------------------------

    print("Confusion Matrix:")

    print(
        confusion_matrix(
            y_valid,
            y_pred
        )
    )


# ============================================================
# 16. MODEL COMPARISON
# ============================================================

results_df = pd.DataFrame(
    results
)


results_df = results_df.sort_values(
    by=[
        "F1 Score",
        "Recall",
        "Precision"
    ],
    ascending=False
)


print("\n")
print("=" * 60)
print("MODEL COMPARISON")
print("=" * 60)


print(
    results_df.to_string(
        index=False
    )
)


# ============================================================
# 17. SELECT BEST MODEL
# ============================================================

best_model_name = (
    results_df.iloc[0]["Model"]
)


best_model = best_models[
    best_model_name
]


print("\n")
print("=" * 60)
print("BEST MODEL SELECTED")
print("=" * 60)


print(
    "Best Model:",
    best_model_name
)


print(
    "Reason: Highest Validation F1 Score"
)


# ============================================================
# 18. FINAL PREDICTION
# ============================================================

final_predictions = best_model.predict(
    X_valid
)


# ============================================================
# 19. FINAL METRICS
# ============================================================

final_accuracy = accuracy_score(
    y_valid,
    final_predictions
)

final_precision = precision_score(
    y_valid,
    final_predictions,
    zero_division=0
)

final_recall = recall_score(
    y_valid,
    final_predictions,
    zero_division=0
)

final_f1 = f1_score(
    y_valid,
    final_predictions,
    zero_division=0
)


# ============================================================
# 20. FINAL CLASSIFICATION REPORT
# ============================================================

print("\n")
print("=" * 60)
print("FINAL CLASSIFICATION REPORT")
print("=" * 60)


print(
    classification_report(
        y_valid,
        final_predictions,
        target_names=[
            "No Attrition",
            "Attrition"
        ],
        zero_division=0
    )
)


# ============================================================
# 21. FINAL CONFUSION MATRIX
# ============================================================

print("\n")
print("=" * 60)
print("FINAL CONFUSION MATRIX")
print("=" * 60)


print(
    confusion_matrix(
        y_valid,
        final_predictions
    )
)


# ============================================================
# 22. FINAL MODEL SUMMARY
# ============================================================

print("\n")
print("=" * 60)
print("FINAL BEST MODEL")
print("=" * 60)


print(
    "Model          :",
    best_model_name
)

print(
    "Accuracy       :",
    round(
        final_accuracy,
        4
    )
)

print(
    "Precision      :",
    round(
        final_precision,
        4
    )
)

print(
    "Recall         :",
    round(
        final_recall,
        4
    )
)

print(
    "F1 Score       :",
    round(
        final_f1,
        4
    )
)


print("\n")
print("=" * 60)
print("FINAL CONCLUSION")
print("=" * 60)


print(
    "The final model was selected based on the highest "
    "Validation F1 Score."
)

print(
    "Attrition Recall was also considered because "
    "Attrition is the minority class."
)