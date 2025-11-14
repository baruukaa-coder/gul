from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.domain.entities import FlowerCreate, FlowerOut, FlowerUpdate
from app.usecase.flower_service import FlowerService
from app.di import get_flower_service

router = APIRouter(prefix="/flowers", tags=["flowers"])

def _get_service():
    return get_flower_service()

@router.post("/", response_model=FlowerOut, status_code=status.HTTP_201_CREATED)
async def create_flower(flower: FlowerCreate, service: FlowerService = Depends(_get_service)):
    return await service.create_flower(flower)

@router.get("/", response_model=List[FlowerOut])
async def list_flowers(service: FlowerService = Depends(_get_service)):
    return await service.list_flowers()

@router.get("/{flower_id}", response_model=FlowerOut)
async def get_flower(flower_id: str, service: FlowerService = Depends(_get_service)):
    flower = await service.get_flower(flower_id)
    if not flower:
        raise HTTPException(status_code=404, detail="Flower not found")
    return flower

@router.put("/{flower_id}", response_model=FlowerOut)
async def update_flower(flower_id: str, flower: FlowerUpdate, service: FlowerService = Depends(_get_service)):
    updated = await service.update_flower(flower_id, flower)
    if not updated:
        raise HTTPException(status_code=404, detail="Flower not found")
    return updated

@router.delete("/{flower_id}")
async def delete_flower(flower_id: str, service: FlowerService = Depends(_get_service)):
    deleted = await service.delete_flower(flower_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Flower not found")
    return {"deleted": True}
