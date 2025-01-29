from pydantic_settings import BaseSettings

from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    CLIENT_ID: str 
    CLIENT_SECRET: str
    REDIRECT_URI: str 
    FATSECRET_URL: str = "https://platform.fatsecret.com/rest/foods/search/v3"
    TOKEN_URL: str = "https://platform.fatsecret.com/oauth/token"
    
settings = Settings()
