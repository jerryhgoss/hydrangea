from datetime import datetime
from typing import Optional

from bson import ObjectId
from dotenv import load_dotenv
from pydantic import BaseModel, Field, root_validator

from .garden import GardenModel

load_dotenv()


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class SensorModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    garden_id: PyObjectId = Field(default_factory=PyObjectId, alias="garden_id")
    interval: float = Field(..., gt=0, description="sensing period")

    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        validate_assignment = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {"name": "Temperature", 
                        "interval": "5.0",
                        "garden_id": "6359d55bff77b777dd5c92e8"
                        }
        }

        @root_validator
        def number_validator(cls, values):
            values["updated_at"] = datetime.now()
            return values


class UpdateSensorModel(BaseModel):
    name: Optional[str]
    interval: Optional[float]
    garden_id: Optional[PyObjectId]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {"example": {"name": "Humidity", "interval": "10.0"}}
