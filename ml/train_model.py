import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, classification_report

import joblib



df = pd.read_csv(
    "data/customers.csv"
)



X = df.drop(
    [
    "user_id",
    "conversion"
    ],
    axis=1
)


y = df["conversion"]



X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)



model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)



model.fit(
    X_train,
    y_train
)



prediction = model.predict(
    X_test
)


print(
"Accuracy:",
accuracy_score(
    y_test,
    prediction
)
)



print(
classification_report(
    y_test,
    prediction
)
)



joblib.dump(
    model,
    "models/intent_model.pkl"
)

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

print(
    importance.sort_values(
        "Importance",
        ascending=False
    )
)

print("Model Saved")