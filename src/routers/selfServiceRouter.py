from fastapi import APIRouter, Response
from endpoints.getStatus import status
from endpoints.getLogs import logFile
from endpoints.putWhitelist import PutWhiteList, update_whitelist

router=APIRouter()

@router.get('/logs')
async def getLogs():
    return await logFile()

@router.get('/status')
async def getStatus():
    return await status()

@router.put("/whitelist",summary="Actualiza la whitelist del servicio")
async def updateWhitelist(whitelist: PutWhiteList):
    update_whitelist(whitelist)
    return Response(status_code=201,content="Lista actualizada")