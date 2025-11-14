from fastapi import FastAPI
from app.adapters.http.flower_router import router as flower_router

def create_app() -> FastAPI:
    app = FastAPI(title="gul_service — Flower Store API")
    app.include_router(flower_router)

    @app.get("/healthz")
    async def health():
        return {"status": "ok"}

    return app
