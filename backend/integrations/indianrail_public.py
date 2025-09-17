import os
import requests

API_KEY = os.getenv("INDIANRAIL_API_KEY")  # must be set in .env or docker-compose
BASE_URL = "https://indianrailapi.com/api/v2"

def get_live_status(train_no: str, date: str):
    url = f"{BASE_URL}/livetrainstatus/apikey/{API_KEY}/trainnumber/{train_no}/date/{date}"
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return r.json()

def get_route(train_no: str):
    url = f"{BASE_URL}/trainroute/apikey/{API_KEY}/trainnumber/{train_no}"
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return r.json()
