import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Garden(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    location: str = Field(...)
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {"name": "Og Garden", "location": "3rd Floor Endcap"}
        }


class GardenUpdate(BaseModel):
    name: Optional[str]
    location: Optional[str]

    class Config:
        schema_extra = {
            "example": {"name": "Don Quixote", "location": "Miguel de Cervantes"}
        }
