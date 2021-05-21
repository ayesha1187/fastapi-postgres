from fastapi import FastAPI
from src.routers import api
import logging
from mangum import Mangum

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = FastAPI()

app.include_router(api.api_router)
handler = Mangum(app)