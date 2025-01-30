from fastapi import FastAPI

from src.routers import food

app = FastAPI()

app.include_router(food.food_router)

@app.get("/")
def health_check():
    return {"status": "ok"}