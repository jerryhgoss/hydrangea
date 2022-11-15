import os
import sys

parent = os.path.abspath(".")
sys.path.append(parent)

from dotenv import dotenv_values
from fastapi import FastAPI
from pymongo import MongoClient

from App.server.routes.garden import router as garden_router

config = dotenv_values(".env")

app = FastAPI()


@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(garden_router, tags=["gardens"], prefix="/garden")
