from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class FlowerCreate(BaseModel):
    name: str = Field(..., example="Rose")
    description: Optional[str] = Field(None, example="A red rose")
    price: float = Field(..., example=3.5)
    stock: int = Field(..., example=100)
    color: Optional[str] = Field(None, example="red")

class FlowerUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    color: Optional[str] = None

class FlowerOut(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    color: Optional[str] = None
    created_at: datetime
