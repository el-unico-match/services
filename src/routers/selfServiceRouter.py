from fastapi import APIRouter
from endpoints.getStatus import status
from endpoints.getLogs import logFile
router=APIRouter()

@router.get('/logs')
async def getLogs():
    return await logFile()

@router.get('/status')
async def getStatus():
    return await status()
    