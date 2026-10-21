from backend.worker.celery_app import app
from backend.app.services.riot_client import get_puuid
from backend.app.services.sync import sync_matches
import os

@app.task(name="sync_new_matches")
def sync_new_matches():
    game_name = os.getenv("RIOT_GAME_NAME")
    tag_line = os.getenv("RIOT_TAG_LINE")
    puuid = get_puuid(game_name, tag_line)
    return sync_matches(puuid, count=20)