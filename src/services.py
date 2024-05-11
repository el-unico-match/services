from fastapi import FastAPI
from middlewares.RequestLogger import RequestLoggerMiddleware
from middlewares.DatabaseExceptionHandlerMiddleware import DatabaseExceptionHandlerMiddleware
from routers import selfServiceRouter
from routers import externalServiceRouter

app = FastAPI()

app.add_middleware(DatabaseExceptionHandlerMiddleware)
app.add_middleware(RequestLoggerMiddleware)

app.include_router(
    router=selfServiceRouter.router,
    prefix='/api/v1'
)

app.include_router(
    router=externalServiceRouter.router, 
    prefix='/api/v1',
)
