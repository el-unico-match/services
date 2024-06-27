
from typing import Any
from repository.database import DatatabaseClient
import re

async def getServices(id, baseUrl, type, apiKeyState, databaseClient: DatatabaseClient) -> Any:

    filter = {}
    
    if ( id != None):
        filter['id'] = id

    if ( baseUrl != None):
        pattern = re.compile(f'.*{baseUrl}.*', re.IGNORECASE)
        filter['baseUrl'] = {'$regex': pattern}

    if ( type != None):
        filter['type'] = type

    if ( apiKeyState != None):
        filter['availability']=apiKeyState

    return await databaseClient.listItems(filter)