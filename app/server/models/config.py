import json as js
from datetime import datetime
from typing import List, Optional, Union

from bson import ObjectId
from dotenv import load_dotenv
from pydantic import BaseModel, Field, root_validator

from .id import PyObjectId

load_dotenv()


from .id import PyObjectId
from .schedules import RAS, SAS, SS


class ConfigModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    garden_id: PyObjectId

    scheduled_actuators: List[SAS] = []
    sensors: List[SS] = []
    reactive_actuators: List[RAS] = []

    created_at: datetime = datetime.now()




    # scheduled_actuators: List[Image] = []

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        validate_assignment = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {"name": "Config1","garden_id": "635ca57475e8e2a0afbe1bd5" ,"reactive_actuators":[{'RAS_id':'635ca57475e8e2a0afbe1bd5', 'interval': '5.0', 'threshold': '3.0', 'duration': '2.0', 'threshold_type': '1'}],
            "sensors":[{'S_id':'635ca57475e8e2a0afbe1bd5','interval':'5.0'}],"scheduled_actuators": [{'SA_id':'635ca57475e8e2a0afbe1bd5','on': ['uu'],'off': ['vv']}]}
        }


