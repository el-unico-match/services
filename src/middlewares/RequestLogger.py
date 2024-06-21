import logging
import uuid
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

logging.basicConfig(filename='log',level=10)
logger=logging.getLogger(__name__)

class RequestLoggerMiddleware(BaseHTTPMiddleware):
    
    async def logRequest(self, request: Request, requestId: uuid):
            data = {
                "requestId" : requestId.hex,
                "client": request.client,
                "method": request.method,
                "url": request.url,
                "body": await request.body(),
                "headers": request.headers.raw,
            }

            requestJson=jsonable_encoder(data);
            logger.info(requestJson)

    async def logResponse(self, response: Response, requestId: uuid):
            data = {
                "requestId" : requestId.hex,
                "statusCode" : response.status_code,
            }

            requestJson=jsonable_encoder(data);
            logger.info(requestJson)

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):

        requestId = uuid.uuid4()

        try:
            await self.logRequest(request, requestId)
            response = await call_next(request)
            await self.logResponse(response, requestId)
            return response

        except Exception as e:
            exceptionJson = jsonable_encoder(e)
            print(exceptionJson)
            logger.error(exceptionJson)

            return Response(content='Internal Server Error', status_code=500)



