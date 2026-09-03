from fastapi import FastAPI

from utils.database import Base, engine
from models.production import ProductionRecord
from api.routers.production import router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Production Records API",
    version="1.0.0",
)


app.include_router(router)
