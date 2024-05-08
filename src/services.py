from fastapi import FastAPI
from middlewares.RequestLogger import RequestLoggerMiddleware
from routers import selfServiceRouter

app = FastAPI()
app.add_middleware(RequestLoggerMiddleware)
app.include_router(selfServiceRouter.router)
