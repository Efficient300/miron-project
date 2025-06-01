from fastapi import FastAPI
from app.api.endpoints.kazik import router as kazik_router


app = FastAPI(title="Kazik API")

app.include_router(kazik_router)