import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

print("===== LOAD DATA =====")
train_df=pd.read_csv("trainmobile.csv")
test_df=pd.read_csv("testmobile.csv")

print("\n===== TRAIN DATA =====")
print(train_df.head())

print("\n===== TRAIN DATA INFORMATION =====")
train_df.info()

print("\n===== TEST DATA =====")
print(test_df.head())

print("\n===== TEST DATA INFORMATION =====")
test_df.info()

print("\n===== MISSING VALUES - TRAIN =====")
print(train_df.isnull().sum())

print("\n===== MISSING VALUES - TEST =====")
print(test_df.isnull().sum())

print("\n===== DUPLICATES =====")
print(
    "Duplicate Rows in train:",
    train_df.duplicated().sum()
)

print(
    "Duplicate Rows in test:",
    test_df.duplicated().sum()
)

train_df=train_df.drop_duplicates()
test_df=test_df.drop_duplicates()

print("\n===== PRICE RANGE DISTRIBUTION =====")
print(
    train_df["price_range"].value_counts().sort_index()
)

print("\n===== FEATURE ENGINEERING =====")
train_df["Pixel_Area"]=(
    train_df["px_height"] *
    train_df["px_width"]
)

test_df["Pixel_Area"]=(
    test_df["px_height"] *
    test_df["px_width"]
)

train_df["Total_Camera"]=(
    train_df["fc"] +
    train_df["pc"]
)

test_df["Total_Camera"]=(
    test_df["fc"] +
    test_df["pc"]
)

train_df["Screen_Area"]=(
    train_df["sc_h"] *
    train_df["sc_w"]
)

test_df["Screen_Area"]=(
    test_df["sc_h"] *
    test_df["sc_w"]
)

train_df["Connectivity_Score"]=(
    train_df["blue"] +
    train_df["dual_sim"] +
    train_df["four_g"] +
    train_df["three_g"] +
    train_df["wifi"] +
    train_df["touch_screen"]
)

test_df["Connectivity_Score"]=(
    test_df["blue"] +
    test_df["dual_sim"] +
    test_df["four_g"] +
    test_df["three_g"] +
    test_df["wifi"] +
    test_df["touch_screen"]
)

train_df["RAM_Per_Weight"]=(
    train_df["ram"] /
    train_df["mobile_wt"]
)

test_df["RAM_Per_Weight"]=(
    test_df["ram"] /
    test_df["mobile_wt"]
)

train_df["Battery_Per_Weight"]=(
    train_df["battery_power"] /
    train_df["mobile_wt"]
)

test_df["Battery_Per_Weight"]=(
    test_df["battery_power"] /
    test_df["mobile_wt"]
)

print("\nNew Features Created:")
print("Pixel_Area")
print("Total_Camera")
print("Screen_Area")
print("Connectivity_Score")
print("RAM_Per_Weight")
print("Battery_Per_Weight")

X=train_df.drop("price_range",axis=1)

Y=train_df["price_range"]

print("\n====== TARGET ======")
print(Y.head())

test_ids=test_df["id"]
test_data=test_df.drop("id",axis=1)

print("\n====== FINAL FEATURES ======")
print(X.columns)

print("\n====== TEST FEATURES ======")
print(test_data.columns)

numerical_columns=X.columns.to_list()
print("\n====== NUMERICAL COLUMNS ======")
print(numerical_columns)

numerical_pipeline=Pipeline(
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

models = {

    "Logistic Regression":

        LogisticRegression(
            max_iter=3000,
            C=1,
            random_state=25
        ),


    "Decision Tree":

        DecisionTreeClassifier(
            max_depth=8,
            min_samples_split=10,
            min_samples_leaf=4,
            random_state=25
        ),


    "Random Forest":

        RandomForestClassifier(
            n_estimators=300,
            max_depth=10,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=25,
            n_jobs=-1
        )

}

X_train,X_validation,Y_train,Y_validation=train_test_split(
    X,
    Y,
    test_size=0.20,
    random_state=25,
    stratify=Y
)

print("\n====== DATA SPLIT ======")
print(
    "Training Rows:",
    len(X_train)
)

print(
    "Validation Rows:",
    len(X_validation)
)

trained_models={}
model_results={}

for model_name, algorithm in models.items():
    print("\n")

    print
    ("=========================")

    print("TRAINING:",model_name)

    print
    ("=========================")

    model_pipeline=Pipeline(
        steps=[
            (
                "preprocessing",
                numerical_pipeline
            ),

            (
                "model",
                algorithm
            )
        ]
    )

    model_pipeline.fit(X_train,Y_train)

    trained_models[model_name] = model_pipeline

    validation_predictions=model_pipeline.predict(
        X_validation
    )

    accuracy=accuracy_score (
        Y_validation,
        validation_predictions
    )

    print("\nCLASSIFICATION REPORT")

    print(
        classification_report(
            Y_validation,
            validation_predictions
        )
    )

    print("\nCONFUSION MATRIX")

    print(
        confusion_matrix(
            Y_validation,
            validation_predictions
        )
    )

    model_results[model_name]=accuracy

print("\n")

print
("=================================")

print("MODEL COMPARISON")

print
("=================================")

for model_name,accuracy in model_results.items():
    print(
        model_name,
        "Accuracy:",
        round(
            accuracy * 100,
            2
        ),
        "%"
    )

best_model_name=max(
    model_results,
    key=model_results.get
)

best_model=trained_models[
    best_model_name
]

print
("\n===============================")

print("BEST MODEL")

print
("=================================")

print(
    "Selected Model:",
    best_model_name
)

print(
    "Validation Accuracy:",
    round(
        model_results[best_model_name]
        * 100,
        2
    ),
    "%"
)

best_model.fit(
    X,
    Y
)

print("\nFinal model trained on complete trainmobile.csv")

test_predictions=best_model.predict(
    test_data
)

print("\n====== TEST PREDICTIONS ======")
print(test_predictions)

print("\nNumber of test predictions:")
print(
    len(test_predictions)
)

print("\n====== PREDICTION DISTRIBUTION ======")

print(
    pd.Series(test_predictions)
    .value_counts()
    .sort_index()
)

submission = pd.DataFrame({

    "id":
        test_ids,

    "price_range":
        test_predictions

})

print("\n====== FINAL SUBMISSION ======")

print(
    submission.head(10)
)

print("\nSubmission Rows:")

print(
    len(submission)
)

print("\nSubmission Columns:")

print(
    submission.columns.tolist()
)

submission.to_csv(
    "mobile_price_predictions.csv",
    index=False
)

print("\n=======================")

print(
    "mobile_price_predictions.csv CREATED SUCCESSFULLY!"
)

print("\n=======================")

print("\nFinal Model:")
print(best_model_name)

print("\nFinal Validation Accuracy:")

print(
    round(
        model_results[best_model_name] * 100,
        2
    ),
    "%"
)






