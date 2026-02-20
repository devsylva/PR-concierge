from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/events")
async def slack_events(request: Request):
    body = await request.json()

    if body.get("type") == "url_verification":
        return {"challenge": body["challenge"]}
    
    return {"ok": True}