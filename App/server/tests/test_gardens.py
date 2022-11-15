import os
import sys

from dotenv import dotenv_values
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pymongo import MongoClient

parent = os.path.abspath(".")
sys.path.append(parent)

from App.server.routes.garden import router as garden_router

app = FastAPI()
config = dotenv_values(".env")
app.include_router(garden_router, tags=["gardens"], prefix="/garden")


@app.on_event("startup")
async def startup_event():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"] + "test"]


@app.on_event("shutdown")
async def shutdown_event():
    app.mongodb_client.close()
    app.database.drop_collection("gardens")


def test_create_garden():
    with TestClient(app) as client:
        response = client.post(
            "/garden/", json={"name": "Don Quixote", "location": "Miguel de Cervantes"}
        )
        assert response.status_code == 201

        body = response.json()
        assert body.get("name") == "Don Quixote"
        assert body.get("location") == "Miguel de Cervantes"
        assert "_id" in body
