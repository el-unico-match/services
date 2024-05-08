import pytz
from datetime import datetime
from pydantic_settings import BaseSettings,SettingsConfigDict

class SettingsLoader(BaseSettings):
    LOG_FILEPATH:str
    LOG_LEVEL:int
    APP_SITE:str
    APP_VERSION:str
    INIT_TIME:str = str(datetime.now(pytz.utc))
	
    model_config = SettingsConfigDict(
        env_file=['../dev.env']
    )	