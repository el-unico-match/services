import logging
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from exceptions.NotFoundException import NotFoundException

logging.basicConfig(filename='log',level=10)
logger=logging.getLogger(__name__)

class DatabaseExceptionHandlerMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):

        try:
            response = await call_next(request)
            return response

        except NotFoundException as e404:
            exceptionJson = jsonable_encoder(e404)
            logger.error(exceptionJson)

            return Response(content='No se encontró el elemento', status_code=404)



