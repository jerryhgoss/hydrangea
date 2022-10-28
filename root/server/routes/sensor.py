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
from server.models.garden import GardenModel, UpdateGardenModel
from server.models.sensor import SensorModel, UpdateSensorModel

router = APIRouter()


client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.college


@router.post("/", response_description="Add new sensor", response_model=SensorModel)
async def create_sensor(sensor: SensorModel = Body(...)):
    sensor = jsonable_encoder(sensor)
    new_sensor = await db["sensors"].insert_one(sensor)
    created_sensor = await db["sensors"].find_one({"_id": new_sensor.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_sensor)


@router.get(
    "/", response_description="List all sensors", response_model=List[SensorModel]
)
async def list_sensors():
    sensors = await db["sensors"].find().to_list(1000)
    return sensors


@router.get(
    "/{id}", response_description="Get a single sensor", response_model=SensorModel
)
async def show_sensor(id: str):
    if (sensor := await db["sensors"].find_one({"_id": id})) is not None:
        return sensor

    raise HTTPException(status_code=404, detail=f"Sensor {id} not found")


@router.put("/{id}", response_description="Update a sensor", response_model=SensorModel)
async def update_sensor(id: str, sensor: UpdateSensorModel = Body(...)):
    sensor = {k: v for k, v in sensor.dict().items() if v is not None}

    if len(sensor) >= 1:
        update_result = await db["sensors"].update_one({"_id": id}, {"$set": sensor})

        if update_result.modified_count == 1:
            if (
                updated_sensor := await db["sensors"].find_one({"_id": id})
            ) is not None:
                return updated_sensor

    if (existing_sensor := await db["sensors"].find_one({"_id": id})) is not None:
        return existing_sensor

    raise HTTPException(status_code=404, detail=f"Sensor {id} not found")


@router.delete("/{id}", response_description="Delete a sensor")
async def delete_sensor(id: str):
    delete_result = await db["sensors"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Sensor {id} not found")