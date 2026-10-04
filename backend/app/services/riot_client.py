import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("RIOT_API_KEY")

REGION = 'europe' 


def get_puuid(game_name: str, tag_line: str) -> str:
    url = (
        f"https://{REGION}.api.riotgames.com"
        f"/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    )
    response = requests.get(url, headers={"X-Riot-Token": API_KEY})
    response.raise_for_status()
    return response.json()["puuid"]



if __name__ == "__main__":
    print(get_puuid("JamieFraser", "Adso"))


def get_match_ids(puuid: str, count: int=20) -> list[str]:
    url = (
        f"https://{REGION}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?queue=420&start=0&{count}=20"
    )
    response = requests.get(url, headers={"X-Riot-Token": API_KEY})
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    puuid = get_puuid("JamieFraser", "Adso")
    print(get_match_ids(puuid, count=5))


def get_match(match_id: str) -> dict:
    url = (
        f"https://{REGION}.api.riotgames.com/lol/match/v5/matches/{match_id}"
    )
    response = requests.get(url, headers={"X-Riot-Token": API_KEY})
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    puuid = get_puuid("JamieFraser", "Adso")
    match_ids = get_match_ids(puuid, count=10)
    match = get_match(match_ids[0])
    print(match.keys())
    info = match["info"]
    print(info.keys())
    print(len(info["participants"]))
    print(info["participants"][0].keys())


def find_player(match: dict, puuid: str) -> dict:
    for player in match["info"]["participants"]:
        if player["puuid"] == puuid:
            return player

me = find_player(match, puuid)
print(me["championName"], me["teamPosition"], me["win"])