from fastapi import FastAPI
from api.endpoints.first_page import router as first_page_router

app = FastAPI()

app.include_router(first_page_router)