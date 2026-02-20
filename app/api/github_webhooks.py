from fastapi import APIRouter, Request

router = APIRouter()

@router.post("")
async def github_webhook(request: Request):
    payload = await request.json()
    #we'll come back to verify signatures later, but for now let's just log the payload
    return {"received": True, "keys": list(payload.keys())[:5]}