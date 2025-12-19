from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import joblib
import os

# মডেল লোড
model = joblib.load("model.pkl")

app = FastAPI()

# Static ফাইল মাউন্ট করা
app.mount("/static", StaticFiles(directory="static"), name="static")

# Home page serve করা
@app.get("/")
def home():
    return FileResponse(os.path.join("static", "index.html"))

# API রুট
class StudyHours(BaseModel):
    hours: float

@app.post("/predict")
def predict(data: StudyHours):
    prediction = model.predict([[data.hours]])
    return {"predicted_score": round(prediction[0], 2)}
