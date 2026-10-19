from fastapi import FastAPI
from backend.app.db import get_champion_stats, get_champion_stats_role, get_rolling_winrate
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="LOL Performance Tracker")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["GET"],
)

@app.get("/test")
def test():
    return {"status:" "ok"}

@app.get("/stats/champion")
def get_stats():
    return get_champion_stats()


@app.get("/stats/role")
def get_stats():
    return get_champion_stats_role()

@app.get("/stats/rolling")
def get_stats():
    return get_rolling_winrate()