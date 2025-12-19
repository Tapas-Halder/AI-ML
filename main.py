from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# মডেল লোড
model = joblib.load("model.pkl")

# ইনপুট ডাটা স্কিমা
class StudyData(BaseModel):
    study_hours: float

# হোম রুট
@app.get("/")
def read_root():
    return {"message": "Study Hours Prediction API"}

# প্রেডিকশন রুট
@app.post("/predict")
def predict_score(data: StudyData):
    pred = model.predict([[data.study_hours]])
    return {"predicted_score": pred[0]}
