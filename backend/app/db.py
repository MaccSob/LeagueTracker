import os

import psycopg
from dotenv import load_dotenv
from psycopg.rows import dict_row

load_dotenv()


def get_connection():
    return psycopg.connect(
        host=os.getenv("POSTGRES_HOST","localhost"),
        port=int(os.getenv("POSTGRES_PORT","5433")),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        row_factory=dict_row
    )

def create_tables(): 
    with get_connection()as conn:
         conn.execute(""" CREATE TABLE IF NOT EXISTS matches ( match_id TEXT PRIMARY KEY, champion TEXT NOT NULL, role TEXT, win BOOLEAN NOT NULL, kills INTEGER NOT NULL, deaths INTEGER NOT NULL, assists INTEGER NOT NULL, duration_s INTEGER NOT NULL, 
 played_at TIMESTAMPTZ NOT NULL ) """)

def get_champion_stats() -> list[dict]:
     with get_connection() as conn:
          rows = conn.execute(""" SELECT
    champion,
    count(*) AS games,
    count(*) FILTER (WHERE win) AS wins,
    ROUND(100.0 * count(*) FILTER (WHERE win) / count(*), 1)::float AS winrate
FROM matches
GROUP BY champion
ORDER BY games DESC;
          """).fetchall()
          return rows

def get_champion_stats_role() -> list[dict]:
     with get_connection() as conn:
          rows = conn.execute(""" SELECT
    role,
    count(*) AS games,
    count(*) FILTER (WHERE win) AS wins,
    ROUND(100.0 * count(*) FILTER (WHERE win) / count(*), 1)::float AS winrate
FROM matches
GROUP BY role
ORDER BY games DESC;
          """).fetchall()
          return rows

def get_hour_stats() -> list[dict]:
     with get_connection() as conn:
          rows = conn.execute("""SELECT 
    EXTRACT(HOUR FROM played_At AT TIME ZONE 'Europe/Warsaw')::int AS hour,
    count(*) as games,
    count(*) FILTER (WHERE win) AS wins,
    ROUND(100.0 * count(*) FILTER (WHERE win) / count(*), 1)::float AS winrate
    FROM matches
GROUP BY hour
HAVING count(*) >= 2 ORDER BY hour;
          """).fetchall()
          return rows
     

def get_rolling_winrate() -> list[dict]:
     with get_connection() as conn:
          rows = conn.execute(""" SELECT
    played_at,
    win,
    ROUND(100.0 * AVG(win::int) OVER (
        ORDER BY played_at
        ROWS BETWEEN 50 PRECEDING AND CURRENT ROW), 1)::float AS rolling_winrate

FROM matches
ORDER BY played_at;
          """).fetchall()
          return rows

def save_match(stats: dict) -> None:
     with get_connection() as conn:
          conn.execute(
               """
               INSERT INTO MATCHES (match_id, champion,role,win,kills,deaths,assists,duration_s,played_at)
               VALUES (%(match_id)s, %(champion)s, %(role)s,%(win)s,%(kills)s,%(deaths)s,%(assists)s,%(duration_s)s,%(played_at)s)
               ON CONFLICT (match_id) DO NOTHING
               """,
               stats,
          )
def match_exists(match_id) -> bool:
     with get_connection() as conn:
          row = conn.execute(
               "SELECT 1 FROM matches WHERE match_id = %(match_id)s",{"match_id": match_id},).fetchone()
          return row is not None
        
      


if __name__ == "__main__":
        create_tables()
        print("Table is ready.")
