from typing import List, Optional
from bson import ObjectId
from datetime import datetime
from app.domain.entities import FlowerCreate, FlowerOut, FlowerUpdate
from app.domain.repository import FlowerRepository

class MongoFlowerRepository(FlowerRepository):
    def __init__(self, db):
        self.collection = db["flowers"]

    def _doc_to_out(self, doc) -> Optional[FlowerOut]:
        if not doc:
            return None
        return FlowerOut(
            id=str(doc.get("_id")),
            name=doc.get("name"),
            description=doc.get("description"),
            price=doc.get("price"),
            stock=doc.get("stock"),
            color=doc.get("color"),
            created_at=doc.get("created_at"),
        )

    async def create(self, flower: FlowerCreate) -> FlowerOut:
        doc = flower.dict()
        doc["created_at"] = datetime.utcnow()
        res = await self.collection.insert_one(doc)
        doc["_id"] = res.inserted_id
        return self._doc_to_out(doc)

    async def list(self) -> List[FlowerOut]:
        cursor = self.collection.find().sort([("created_at", -1)])
        docs = await cursor.to_list(length=100)
        return [self._doc_to_out(d) for d in docs]

    async def get(self, flower_id: str) -> Optional[FlowerOut]:
        try:
            oid = ObjectId(flower_id)
        except Exception:
            return None
        doc = await self.collection.find_one({"_id": oid})
        return self._doc_to_out(doc)

    async def update(self, flower_id: str, flower: FlowerUpdate) -> Optional[FlowerOut]:
        try:
            oid = ObjectId(flower_id)
        except Exception:
            return None
        update_doc = {k: v for k, v in flower.dict().items() if v is not None}
        if not update_doc:
            return await self.get(flower_id)
        await self.collection.update_one({"_id": oid}, {"$set": update_doc})
        return await self.get(flower_id)

    async def delete(self, flower_id: str) -> bool:
        try:
            oid = ObjectId(flower_id)
        except Exception:
            return False
        res = await self.collection.delete_one({"_id": oid})
        return res.deleted_count > 0
