# ===============================
# model.py 
# ===============================

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score


def train_model():

    # ===============================
    # LOAD DATASET
    # ===============================
    df = pd.read_csv("student_dropout_FINAL_1000.csv")

    # ===============================
    # FEATURES / TARGET
    # ===============================
    X = df.drop(
        ["student_id", "dropout_risk"],
        axis=1
    )

    y = df["dropout_risk"]

    # ===============================
    # ONE HOT ENCODING
    # ===============================
    X = pd.get_dummies(X)

    # ===============================
    # TRAIN TEST SPLIT
    # ===============================
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    # ===============================
    # MODELS
    # ===============================
    models = {

        "Decision Tree": DecisionTreeClassifier(
            max_depth=6,
            random_state=42
        ),

        "Random Forest": RandomForestClassifier(
            n_estimators=200,
            max_depth=8,
            random_state=42
        ),

        "Logistic Regression": LogisticRegression(
            max_iter=2000
        )
    }

    # ===============================
    # COMPARE MODELS
    # ===============================
    results = {}

    best_model = None
    best_name = ""
    best_score = 0

    for name, model in models.items():

        model.fit(X_train, y_train)

        pred = model.predict(X_test)

        score = accuracy_score(
            y_test,
            pred
        )

        results[name] = round(score, 4)

        if score > best_score:
            best_score = score
            best_model = model
            best_name = name

    # ===============================
    # RETURN
    # ===============================
    return (
        best_model,
        df,
        X.columns,
        X_test,
        y_test,
        best_score,
        best_name,
        results
    )