import os
import sys

from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

sys.path.append("../../server")
from dotenv import load_dotenv

load_dotenv()
from typing import List

import motor.motor_asyncio
from fastapi import Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from server.models.scheduled_actuator import ScheduledActuatorModel

router = APIRouter()


from server.database import db

@router.post("/", response_description="Add new scheduled actuators", response_model=ScheduledActuatorModel)
async def create_sa(sa: ScheduledActuatorModel = Body(...)):
    sa = jsonable_encoder(sa)
    new_sa = await db["sa"].insert_one(sa)
    created_sa = await db["sa"].find_one({"_id": new_sa.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_sa)

@router.get(
    "/", response_description="List all scheduled actuators", response_model=List[ScheduledActuatorModel]
)
async def list_sa():
    SAs = await db["sa"].find().to_list(1000)
    return SAs

@router.get(
    "/{id}", response_description="Get a single scheduled actuator", response_model=ScheduledActuatorModel
)
async def show_sa(id: str):
    if (sa := await db["sa"].find_one({"_id": id})) is not None:
        return sa

    raise HTTPException(status_code=404, detail=f"Scheduled actuator {id} not found")



