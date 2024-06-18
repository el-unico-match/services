from fastapi import FastAPI
from middlewares.RequestLogger import RequestLoggerMiddleware
from middlewares.DatabaseExceptionHandlerMiddleware import DatabaseExceptionHandlerMiddleware
from routers import selfServiceRouter
from routers import externalServiceRouter
from configs.settings import settings
import logging

logging.info(f"Starting application at {settings.INIT_TIME}")

app=FastAPI(
    title="services",
    version="0.0.1",
    summary='Manages services',
    docs_url='/api-docs'
)

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
