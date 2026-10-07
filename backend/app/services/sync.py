from backend.app.services.riot_client import get_puuid,get_match_ids,get_match,extract_stats
from backend.app.db import save_match

def sync_matches(puuid: str, count: int = 20) -> int:
    saved = 0
    for match_id in get_match_ids(puuid, count):
        match = get_match(match_id)
        stats = extract_stats(match, puuid)
        save_match(stats)
        saved += 1
        return saved