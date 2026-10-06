import os

import psycopg
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return psycopg.connect(
        host="localhost",
        port=5433,
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
    )

def create_tables(): 
    with get_connection()as conn:
         conn.execute(""" CREATE TABLE IF NOT EXISTS matches ( match_id TEXT PRIMARY KEY, champion TEXT NOT NULL, role TEXT, win BOOLEAN NOT NULL, kills INTEGER NOT NULL, deaths INTEGER NOT NULL, assists INTEGER NOT NULL, duration_s INTEGER NOT NULL, 
 played_at TIMESTAMPTZ NOT NULL ) """)


if __name__ == "__main__":
        create_tables()
        print("Table is ready.")
