from dotenv import load_dotenv

import sys
from fastapi import FastAPI

from server.routes.config import router as ConfigRouter
from server.routes.garden import router as GardenRouter
from server.routes.sensor import router as SensorRouter
from server.routes.sa import router as SARouter
from server.routes.ra import router as RARouter

sys.path.append("../server")
load_dotenv()


app = FastAPI()

app.include_router(GardenRouter, tags=["Garden"], prefix="/Garden")

app.include_router(SensorRouter, tags=["Sensor"], prefix="/Sensor")

app.include_router(ConfigRouter, tags=["Config"], prefix="/Config")

app.include_router(SARouter, tags=["SA"], prefix="/SA")

app.include_router(RARouter, tags=["RA"], prefix="/RA")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the 2022-23 Hydro API!"}
