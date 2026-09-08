import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.impute import SimpleImputer

from sklearn.preprocessing import OneHotEncoder

from sklearn.compose import ColumnTransformer

from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

train_df = pd.read_csv("train.csv")

test_df = pd.read_csv("test.csv")


print("\n================ TRAIN DATA ================")

print(train_df.head())

print("\nTRAIN DATA INFORMATION")

train_df.info()


print("\n================ TEST DATA ================")

print(test_df.head())

print("\nTEST DATA INFORMATION")

test_df.info()

print("\n================ MISSING VALUES - TRAIN ================")

print(train_df.isnull().sum())


print("\n================ MISSING VALUES - TEST ================")

print(test_df.isnull().sum())

print("\n================ DUPLICATES ================")

print("Duplicate rows in train:", train_df.duplicated().sum())

print("Duplicate rows in test:", test_df.duplicated().sum())

train_df = train_df.drop_duplicates()

test_df = test_df.drop_duplicates()

print("\n================ FEATURE ENGINEERING ================")

train_df["FamilySize"] = (
    train_df["SibSp"] +
    train_df["Parch"] +
    1
)

test_df["FamilySize"] = (
    test_df["SibSp"] +
    test_df["Parch"] +
    1
)

train_df["IsAlone"] = (
    train_df["FamilySize"] == 1
).astype(int)

test_df["IsAlone"] = (
    test_df["FamilySize"] == 1
).astype(int)

train_df["Title"] = (
    train_df["Name"]
    .str.extract(r",\s*([^.]*)\.", expand=False)
    .str.strip()
)

test_df["Title"] = (
    test_df["Name"]
    .str.extract(r",\s*([^.]*)\.", expand=False)
    .str.strip()
)

common_titles = [
    "Mr",
    "Miss",
    "Mrs",
    "Master"
]


train_df["Title"] = train_df["Title"].where(
    train_df["Title"].isin(common_titles),
    "Rare"
)

test_df["Title"] = test_df["Title"].where(
    test_df["Title"].isin(common_titles),
    "Rare"
)

train_df["FarePerPerson"] = (
    train_df["Fare"] /
    train_df["FamilySize"]
)

test_df["FarePerPerson"] = (
    test_df["Fare"] /
    test_df["FamilySize"]
)


print("\nNew features created:")

print("FamilySize")

print("IsAlone")

print("Title")

print("FarePerPerson")

X = train_df.drop(
    "Survived",
    axis=1
)

Y = train_df["Survived"]


print("\n================ TARGET ================")

print(Y.head())

columns_to_drop = [
    "PassengerId",
    "Name",
    "Ticket",
    "Cabin"
]


X = X.drop(
    columns=columns_to_drop
)

test_data = test_df.drop(
    columns=columns_to_drop
)


print("\n================ FINAL FEATURES ================")

print(X.columns)


print("\n================ TEST FEATURES ================")

print(test_data.columns)

numerical_columns = [
    "Age",
    "SibSp",
    "Parch",
    "Fare",
    "Pclass",
    "FamilySize",
    "IsAlone",
    "FarePerPerson"
]

categorical_columns = [
    "Sex",
    "Embarked",
    "Title"
]


print("\n================ NUMERICAL COLUMNS ================")

print(numerical_columns)


print("\n================ CATEGORICAL COLUMNS ================")

print(categorical_columns)

numerical_pipeline = Pipeline(
    steps=[

        (
            "imputer",
            SimpleImputer(
                strategy="median"
            )
        )

    ]
)


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
                handle_unknown="ignore"
            )
        )

    ]
)

preprocessor = ColumnTransformer(
    transformers=[

        (
            "num",
            numerical_pipeline,
            numerical_columns
        ),

        (
            "cat",
            categorical_pipeline,
            categorical_columns
        )

    ]
)

models = {

    "Logistic Regression":

        LogisticRegression(
            max_iter=2000,
            C=1,
            random_state=25
        ),


    "Decision Tree":

        DecisionTreeClassifier(
            max_depth=5,
            min_samples_split=10,
            min_samples_leaf=4,
            random_state=25
        ),


    "Random Forest":

        RandomForestClassifier(
            n_estimators=300,
            max_depth=7,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=25
        )
}

X_train, X_validation, Y_train, Y_validation = train_test_split(

    X,
    Y,

    test_size=0.20,

    random_state=25,

    stratify=Y
)


print("\n================ DATA SPLIT ================")

print("Training Rows:", len(X_train))

print("Validation Rows:", len(X_validation))

trained_models = {}

model_results = {}


for model_name, algorithm in models.items():

    print("\n")
    print("==============================================")

    print("TRAINING:", model_name)

    print("==============================================")


    model_pipeline = Pipeline(
        steps=[

            (
                "preprocessing",
                preprocessor
            ),

            (
                "model",
                algorithm
            )

        ]
    )


    model_pipeline.fit(
        X_train,
        Y_train
    )

    trained_models[model_name] = model_pipeline


    validation_predictions = model_pipeline.predict(
        X_validation
    )

    accuracy = accuracy_score(
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

    model_results[model_name] = accuracy

print("\n")

print("===================================")

print("MODEL COMPARISON")

print("==============================")


for model_name, accuracy in model_results.items():

    print(
        model_name,
        "Accuracy:",
        round(accuracy * 100, 2),
        "%"
    )


best_model_name = max(
    model_results,
    key=model_results.get
)


best_model = trained_models[
    best_model_name
]


print("\n===================================")

print("BEST MODEL")

print("=====================================")

print("Selected Model:", best_model_name)

print(
    "Validation Accuracy:",
    round(
        model_results[best_model_name] * 100,
        2
    ),
    "%"
)


best_model.fit(
    X,
    Y
)


print("\nFinal model trained on complete train.csv")


test_predictions = best_model.predict(
    test_data
)


print("\n================ TEST PREDICTIONS ================")

print(test_predictions)


print("\nNumber of test predictions:")

print(len(test_predictions))

submission = pd.DataFrame({

    "PassengerId":
        test_df["PassengerId"],

    "Survived":
        test_predictions

})


print("\n================ SUBMISSION ================")

print(submission.head())

print("\nSubmission Rows:")

print(len(submission))

submission.to_csv(
    "gender_submission1.csv",
    index=False
)


print("\n===================================")

print("gender_submission1.csv CREATED SUCCESSFULLY!")

print("=====================================")


print("\nFinal Model:")

print(best_model_name)



