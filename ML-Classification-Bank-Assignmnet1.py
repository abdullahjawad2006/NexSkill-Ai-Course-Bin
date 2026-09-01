import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.preprocessing import OneHotEncoder

from sklearn.compose import ColumnTransformer

from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression

from sklearn.ensemble import RandomForestClassifier

from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import classification_report

from sklearn.metrics import confusion_matrix


df=pd.read_csv('bank.csv')

print(df.head())

print(df.info())

print(df.describe())


X=df.drop("deposit",axis=1)

Y=df["deposit"].map({
    "no":0,
    "yes":1
})


print("X:")

print(X)

print("Y:")

print(Y)


numerical_columns=X.select_dtypes(include=["int64","float64"]).columns

categorical_columns=X.select_dtypes(include=["object"]).columns


print("Numnerical Columns:")

print(numerical_columns)

print("Categorical Columns:")

print(categorical_columns)


X_train,X_test,Y_train,Y_test=train_test_split(
    X,
    Y,
    train_size=0.70,
    random_state=25,
    stratify=Y
)


print("Training Rows:",len(X_train))

print("Testing Rows:",len(X_test))


preprocessor=ColumnTransformer(
    transformers=[
        ("num",StandardScaler(),numerical_columns),
        ("cat",OneHotEncoder(handle_unknown="ignore"),categorical_columns)
    ]
)


logistic_model=Pipeline(
    steps=[
        ("preprocessing",preprocessor),
        ("model",LogisticRegression(max_iter=1000))
    ]
)


random_forest_model=Pipeline(
    steps=[
        ("preprcessing",preprocessor),
        ("model",RandomForestClassifier(
            n_estimators=300,
            random_state=25
        ))
    ]
)


decision_tree_model=Pipeline(
    steps=[
        ("preprocessing",preprocessor),
        ("model",DecisionTreeClassifier(
            random_state=25
        ))
    ]
)


logistic_model.fit(X_train,Y_train)

random_forest_model.fit(X_train,Y_train)

decision_tree_model.fit(X_train,Y_train)


logistic_predictions=logistic_model.predict(X_test)

random_forest_predictions=random_forest_model.predict(X_test)

decision_tree_predictions=decision_tree_model.predict(X_test)


print("LOGISTIC REGRESSION")

print("\nClassification Report:")

print(classification_report(Y_test,logistic_predictions))

print("Confusion Matrix:")

print(confusion_matrix(Y_test,logistic_predictions))


print("RANDOM FOREST")

print("\nClassification Report:")

print(classification_report(
    Y_test,
    random_forest_predictions
))

print("Confusion Matrix:")

print(confusion_matrix(
    Y_test,
    random_forest_predictions
))


print("DECISION TREE")

print("\nClassification Report:")

print(classification_report(
    Y_test,
    decision_tree_predictions
))

print("Confusion Matrix:")

print(confusion_matrix(
    Y_test,
    decision_tree_predictions
))



