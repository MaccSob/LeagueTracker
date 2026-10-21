from celery import Celery
import os


app = Celery(
    "worker",
    broker=os.getenv("REDIS_URL", "redis://localhost:6379/0"),
    include=["backend.worker.tasks"],
)


app.conf.beat_schedule = {
    "sync-matches": {
        "task": "sync_new_matches",
        "schedule": 21600,
    },
}