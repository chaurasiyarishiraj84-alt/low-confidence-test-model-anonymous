from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
async def predict(data: dict = None):
    return {
        "prediction": random.choice(["uncertain", "unknown"]),
        "confidence": round(random.uniform(0.10, 0.30), 3)
    }