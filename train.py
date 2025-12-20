import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# data
data = {
    "study_hours": [1, 2, 3, 4, 5],
    "score": [10, 20, 30, 40, 50]
}

df = pd.DataFrame(data)

X = df[["study_hours"]]
y = df["score"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")
