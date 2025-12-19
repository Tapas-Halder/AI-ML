from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# মডেল লোড
model = joblib.load("model.pkl")

app = FastAPI()

# ইনপুটের জন্য স্কিমা
class StudyHours(BaseModel):
    hours: float

# প্রেডিকশন রুট
@app.post("/predict")
def predict(data: StudyHours):
    prediction = model.predict([[data.hours]])
    return {"predicted_score": prediction[0]}
