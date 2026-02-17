from fastapi import FastAPI, Depends, HTTPException
from aerostack import Aerostack
from pydantic import BaseModel
import os

"""
FastAPI Integration Example

Demonstrates how to use the Aerostack Python SDK with FastAPI, 
utilizing its dependency injection system.
"""

app = FastAPI()

# Dependency to get SDK instance
def get_sdk():
    # You could also use lru_cache for singleton behavior
    return Aerostack(
        # api_key_auth=os.environ.get("AEROSTACK_API_KEY")
    )

class SignupRequest(BaseModel):
    email: str
    password: str
    name: str

@app.post("/signup")
async def signup(req: SignupRequest, sdk: Aerostack = Depends(get_sdk)):
    try:
        res = sdk.authentication.auth_signup(
            request={
                "email": req.email,
                "password": req.password,
                "name": req.name
            }
        )
        
        # Note: Speakeasy SDKs often throw on non-2xx default, check docs
        # Here we assume it returns a response object we can check
        return res.auth_signup_response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health(sdk: Aerostack = Depends(get_sdk)):
    try:
        res = sdk.database.db_query(request={"query": "SELECT 1"})
        return {"status": "ok", "db": res.db_query_response}
    except Exception:
        return {"status": "error"}
