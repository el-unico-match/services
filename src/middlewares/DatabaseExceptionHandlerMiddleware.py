import logging
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from exceptions.NotFoundException import NotFoundException
from exceptions.ForbiddenException import ForbiddenException
from exceptions.ValidationException import ValidationException

logger=logging.getLogger(__name__)

class DatabaseExceptionHandlerMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):

        try:
            response = await call_next(request)
            return response

        except ForbiddenException as e403:
            exceptionJson = jsonable_encoder(e403)
            logger.error(exceptionJson)

            return Response(content='No tiene permisos para realizar la acción.', status_code=403)

        except NotFoundException as e404:
            exceptionJson = jsonable_encoder(e404)
            logger.error(exceptionJson)

            return Response(content='No se encontró el elemento', status_code=404)

        except ValidationException as e422:
            exceptionJson = jsonable_encoder(e422)
            logger.error(exceptionJson)

            return Response(content=e422.message, status_code=422)
        
        except Exception as e500:
            exceptionJson = jsonable_encoder(e500)
            logger.error(exceptionJson)

            return Response(content='Lo sentimos, algo falló', status_code=500)

