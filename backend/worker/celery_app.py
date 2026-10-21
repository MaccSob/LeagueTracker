from celery import Celery

app = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    include=["backend.worker.tasks"],
)


app.conf.beat_schedule = {
    "sync-matches": {
        "task": "sync_new_matches",
        "schedule": 60,
    },
}