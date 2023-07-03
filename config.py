from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGODB_URI: str 
   
# specify .env file location as Config attribute
    class Config:
        env_file = ".env"
    
settings = Settings()