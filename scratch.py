from backend.app.services.riot_client import get_puuid,get_match_ids,get_match,extract_stats
from backend.app.db import save_match, match_exists
from backend.app.services.sync import sync_matches

puuid = get_puuid("JamieFraser", "Adso")
print(sync_matches(puuid, count=50))