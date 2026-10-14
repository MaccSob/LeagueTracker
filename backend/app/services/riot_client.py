import os
import requests
from dotenv import load_dotenv
from datetime import datetime,timezone
import time

load_dotenv()

API_KEY = os.getenv("RIOT_API_KEY")

REGION = 'europe' 


def get_puuid(game_name: str, tag_line: str) -> str:
    url = (
        f"https://{REGION}.api.riotgames.com"
        f"/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    )
    return riot_get(url)



if __name__ == "__main__":
    print(get_puuid("JamieFraser", "Adso"))


def get_match_ids(puuid: str, count: int=20) -> list[str]:
    url = (
        f"https://{REGION}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?queue=420&start=0&count={count}"
    )
    return riot_get(url)


if __name__ == "__main__":
    puuid = get_puuid("JamieFraser", "Adso")
    print(get_match_ids(puuid, count=5))


def get_match(match_id: str) -> dict:
    url = (
        f"https://{REGION}.api.riotgames.com/lol/match/v5/matches/{match_id}"
    )
    return riot_get(url)


if __name__ == "__main__":
    puuid = get_puuid("JamieFraser", "Adso")
    match_ids = get_match_ids(puuid, count=10)
    match = get_match(match_ids[0])
    print(match.keys())
    info = match["info"]


def find_player(match: dict, puuid: str) -> dict:
    for player in match["info"]["participants"]:
        if player["puuid"] == puuid:
            return player

def riot_get(url):
    for attempt in range(5):
        response = requests.get(url, headers={"X-Riot-Token": API_KEY})
        if response.status_code == 429:
            trier = response.headers["Retry-After"]
            time.sleep(int(trier))
            continue
        response.raise_for_status()
        return response.json()
    raise RuntimeError('Finished')


def extract_stats(match: dict, puuid: str) -> dict:
    me = find_player(match, puuid)
    return {
        "match_id": match["metadata"]["matchId"],
        "champion": me["championName"],
        "role": me["role"],
        "win": me["win"],
        "kills": me["kills"],
        "deaths": me["deaths"],
        "assists": me["assists"],
        "duration_s": match["info"]["gameDuration"],
        "played_at": datetime.fromtimestamp(match["info"]["gameCreation"]/1000, tz=timezone.utc)
    }

if __name__ == "__main":
    puuid = get_puuid("JamieFraser", "Adso")
    match_ids = get_match_ids(puuid, count=1)
    match = get_match(match_ids[0])
    print(extract_stats(match, puuid))