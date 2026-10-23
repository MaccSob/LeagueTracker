from backend.app.services.riot_client import get_puuid,get_match_ids,get_match,extract_stats
from backend.app.db import save_match, match_exists, get_champion_stats, get_champion_stats_role, get_hour_stats
from backend.app.services.sync import sync_matches

for row in get_hour_stats():
    print(row)