from fastapi import FastAPI

from palimpsest.api.v1.router import router as v1_router

app = FastAPI(
    title="Palimpsest API",
    version="0.1.0",
)

app.include_router(v1_router)
