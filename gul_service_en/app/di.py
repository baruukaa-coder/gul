from app.adapters.repo.mongo_flower_repo import MongoFlowerRepository
from app.usecase.flower_service import FlowerService
from app.infrastructure.db import get_db

def get_flower_service():
    """Simple factory for FlowerService used by FastAPI dependencies."""
    db = get_db()
    repo = MongoFlowerRepository(db)
    return FlowerService(repo)
