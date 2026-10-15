from fastapi import FastAPI

app = FastAPI(title="LOL Performance Tracker")


@app.get("/test")
def test():
    return {"status:" "ok"}