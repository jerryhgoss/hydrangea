from enum import Enum, IntEnum
from typing import List, Optional, Union

from pydantic import BaseModel, Field, root_validator

from .id import PyObjectId


class SS(BaseModel):
    S_id: PyObjectId = Field(alias="S_id")
    interval: float

class SAS(BaseModel):
    SA_id: PyObjectId = Field(alias="SA_id")
    on: List[str] = []
    off: List[str] = []

class RAS(BaseModel):
    RAS_id: PyObjectId
    interval: float = Field(gt=0, description="Checking Period")
    threshold: float = Field(gt=0, description="Threshold ActivationValue")
    duration: float = Field(gt=0, description="How long to Actuate for")
    threshold_type: int