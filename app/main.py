from fastapi import FastAPI
from app.routes import image_routes

app = FastAPI()

app.include_router(image_routes.router)
