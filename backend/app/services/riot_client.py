import os
import requests
from dotenv import load_dotenv

load_dotenv

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
    print(get_puuid("UserName", "TAG"))






