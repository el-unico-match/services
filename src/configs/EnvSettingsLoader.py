import pytz
from datetime import datetime
from pydantic_settings import BaseSettings,SettingsConfigDict

class SettingsLoader(BaseSettings):
    LOG_FILEPATH:str
    LOG_LEVEL:int

    APP_SITE:str
    APP_VERSION:str
    
    INIT_TIME:str = str(datetime.now(pytz.utc))
	
    DB_HOST:str
    DB_PORT:int

    model_config = SettingsConfigDict()	