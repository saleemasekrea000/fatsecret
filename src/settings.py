from pydantic_settings import BaseSettings

from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    client_id: str
    client_secret: str
    fatsecret_url: str = "https://platform.fatsecret.com/rest/server.api"
    fatsecret_auth_url: str = "https://platform.fatsecret.com/oauth/authenticate"
    access_token_url: str = "https://oauth.fatsecret.com/connect/token"
    grant_type:str = "client_credentials" 

settings = Settings()
