from backend.app.services.riot_client import get_puuid,get_match_ids,get_match,extract_stats
from backend.app.db import save_match, match_exists, get_champion_stats
from backend.app.services.sync import sync_matches

puuid = get_puuid("papi", "bd01")
print(sync_matches(puuid, count=50))
print(get_champion_stats())