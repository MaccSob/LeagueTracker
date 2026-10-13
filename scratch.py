from backend.app.services.riot_client import get_puuid,get_match_ids,get_match,extract_stats
from backend.app.db import save_match, match_exists
from backend.app.services.sync import sync_matches

puuid = get_puuid("JamieFraser", "Adso")
match_ids = get_match_ids(puuid, count=1)
match = get_match(match_ids[0])
stats = extract_stats(match, puuid)
save_match(stats)
print("Saved", stats["match_id"])

print(match_exists("EUW1_8004962271"))
print(match_exists("EUN1_0"))
puuid(get_puiid("JamieFraser", "Adso"))
print(sync_matches(puuid, count=5))