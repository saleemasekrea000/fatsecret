import requests

from src.schemas import FoodSearchRequest
from src.utility import get_access_token
from src.settings import settings

def search_foods(request_params: FoodSearchRequest):
    url = f"{settings.fatsecret_url}/search_foods"
    
    token = get_access_token()
    if not token:
        raise ValueError("Failed to retrieve access token")

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    try:
        response = requests.post(url, headers=headers, params=request_params.dict())
        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        return {"error": "Request failed", "details": str(e)}
    except ValueError as e:
        return {"error": "Invalid response format", "details": str(e)}