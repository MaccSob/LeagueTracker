from fastapi import FastAPI
from backend.app.db import get_champion_stats, get_champion_stats_role

app = FastAPI(title="LOL Performance Tracker")


@app.get("/test")
def test():
    return {"status:" "ok"}

@app.get("/stats/champion")
def get_stats():
    return get_champion_stats()


@app.get("/stats/role")
def get_stats():
    return get_champion_stats_role()