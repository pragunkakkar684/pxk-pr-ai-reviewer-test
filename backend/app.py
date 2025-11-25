from fastapi import FastAPI, Request
import hmac
import hashlib
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

GITHUB_SECRET = os.getenv("GITHUB_WEBHOOK_SECRET")

@app.post("/webhook")
async def github_webhook(request: Request):
    body = await request.body()
    
    # Validate signature
    signature = request.headers.get("X-Hub-Signature-256")
    computed = "sha256=" + hmac.new(
        GITHUB_SECRET.encode(), body, hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(signature, computed):
        return {"status": "invalid signature"}

    payload = await request.json()

    print("\n--- WEBHOOK RECEIVED ---")
    print(payload)

    return {"status": "ok"}
