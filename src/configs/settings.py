import pytz
from datetime import datetime
from pydantic_settings import BaseSettings,SettingsConfigDict

class SettingsLoader(BaseSettings):
    LOG_FILEPATH:str='log.txt'
    LOG_LEVEL:int=10

    APP_SITE:str='localhost:4003'
    APP_VERSION:str='lastest_commit'
    
    INIT_TIME:str = str(datetime.now(pytz.utc))
	
    jwt_private_key:str='private_key'
    jwt_public_key:str='public_key'
    jwt_algorithm:str='HS256'

    db_schema:str='mongodb'
    db_credentials:str='username:password'
    db_domain:str='localhost'
    db_port:int=5003
    db_name:str='dbname'
    
    database_url:str=''
    model_config = SettingsConfigDict(env_file=('../dev.env','.env'))

def loadSettings():
     settings=SettingsLoader()
     settings.database_url=f"{settings.db_schema}://{settings.db_credentials}@{settings.db_domain}:{settings.db_port}/{settings.db_name}"
     return settings

settings=loadSettings()