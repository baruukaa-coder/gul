from typing import List, Optional
from app.domain.entities import FlowerCreate, FlowerOut, FlowerUpdate
from app.domain.repository import FlowerRepository

class FlowerService:
    def __init__(self, repo: FlowerRepository):
        self.repo = repo

    async def create_flower(self, flower: FlowerCreate) -> FlowerOut:
        return await self.repo.create(flower)

    async def list_flowers(self) -> List[FlowerOut]:
        return await self.repo.list()

    async def get_flower(self, flower_id: str) -> Optional[FlowerOut]:
        return await self.repo.get(flower_id)

    async def update_flower(self, flower_id: str, flower: FlowerUpdate) -> Optional[FlowerOut]:
        return await self.repo.update(flower_id, flower)

    async def delete_flower(self, flower_id: str) -> bool:
        return await self.repo.delete(flower_id)
