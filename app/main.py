from fastapi import FastAPI
from app.api.github_webhooks import router as github_router
from app.api.slack_events import router as slack_router

app = FastAPI(title="PR Concierge", version="0.1.0")

@app.get("/health")
def health_check():
    return {"status": "ok :)"}


app.include_router(github_router, prefix="/webhooks/github", tags=["github"])
app.include_router(slack_router, prefix="/slack", tags=["slack"])