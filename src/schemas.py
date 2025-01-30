from pydantic import BaseModel


class FoodSearchRequest(BaseModel):
   method: str
   search_expression: str | None = None
   page_number: int | None = 0
   max_results: int | None = 20
   include_sub_categories: bool | None = False
   include_food_images: bool | None = False
   include_food_attributes: bool | None = False
   flag_default_serving: bool | None = False
   region: str | None = None
   language: str | None = None
   format: str | None = "json"