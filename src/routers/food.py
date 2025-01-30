import requests

from fastapi import APIRouter
from fastapi import HTTPException


from src.schemas import FoodSearchRequest
from src.services.food import search_foods


food_router = APIRouter(
    prefix="/food",
    tags=["food"],
)


@food_router.post("/search_food")
async def search_food(request: FoodSearchRequest):
    return search_foods(request)

