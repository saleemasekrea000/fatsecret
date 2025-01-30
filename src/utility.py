import requests

from fastapi import HTTPException

from src.settings import settings


def get_access_token():

    auth = (settings.client_id, settings.client_secret)
    payload = {
        "grant_type": "client_credentials",
        "scope": "basic"
    }
    
    try:
        response = requests.post(url=settings.access_token_url, data=payload, auth=auth)
        response.raise_for_status() 
        return response.json().get("access_token")
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Request failed: {e}")