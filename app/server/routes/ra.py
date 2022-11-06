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
from server.models.reactive_actuator import ReactiveActuatorModel

router = APIRouter()


from server.database import db


@router.post("/", response_description="Add new reactive actuators", response_model=ReactiveActuatorModel)
async def create_ra(ra: ReactiveActuatorModel = Body(...)):
    ra = jsonable_encoder(ra)
    new_ra = await db["ra"].insert_one(ra)
    created_ra = await db["ra"].find_one({"_id": new_ra.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_ra)


@router.get(
    "/", response_description="List all reactive actuators", response_model=List[ReactiveActuatorModel]
)
async def list_ra():
    RAs = await db["ra"].find().to_list(1000)
    return RAs

@router.get(
    "/{id}", response_description="Get a single reactive actuator", response_model=ReactiveActuatorModel
)
async def show_ra(id: str):
    if (ra := await db["ra"].find_one({"_id": id})) is not None:
        return ra

    raise HTTPException(status_code=404, detail=f"Reactive actuator {id} not found")

