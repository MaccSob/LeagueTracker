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

