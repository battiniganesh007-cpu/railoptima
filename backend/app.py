import os
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Try importing real API
API_KEY = os.getenv("INDIANRAIL_API_KEY")
use_simulation = not bool(API_KEY)

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/status")
def status():
    return {"status": "ok", "mode": "simulation" if use_simulation else "live"}

@app.get("/trains")
def get_trains():
    # Simulation mode → return CSV data
    df = pd.read_csv("data/simulated_trains.csv")
    return df.to_dict(orient="records")

@app.get("/section")
def section():
    if use_simulation:
        df = pd.read_csv("data/simulated_trains.csv")
        return {"section_trains": df.to_dict(orient="records")}
    else:
        return {"error": "Live mode not enabled. Please add API key."}
