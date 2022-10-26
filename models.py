from datetime import datetime
from tokenize import Name
from MySQLdb import DATETIME, Timestamp
from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional
import sqlalchemy
from enum import Enum

class SensorType(str, Enum): 
    pH = "pH"
    ec = "ec"
    temp = "temp"
    level = "level"

class Sensor(BaseModel):
    Id : Optional[UUID] = uuid4()
    Type : SensorType
    Garden_Id : int
    Interval : Optional[float] = None
    #Created_at : Optional[DATETIME] = (datetime.now()).strftime('%Y-%m-%d %H:%M:%S')

class SensorReading(BaseModel):
    Id : int
    Name : str
    Garden_Id : int
    Sensor_Id : UUID
    Value : float
    Created_at : Optional[DATETIME] = (datetime.now()).strftime('%Y-%m-%d %H:%M:%S')





