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
from server.models.config import ConfigModel
from server.models.garden import GardenModel, UpdateGardenModel

router = APIRouter()


from server.database import db


@router.post("/", response_description="Add new config", response_model=ConfigModel)
async def create_config(config: ConfigModel = Body(...)):
    config = jsonable_encoder(config)
    new_config = await db["configs"].insert_one(config)
    created_config = await db["configs"].find_one({"_id": new_config.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_config)

@router.get(
    "/", response_description="List all configs", response_model=List[ConfigModel]
)
async def list_config():
    config = await db["configs"].find().to_list(1000)
    return config