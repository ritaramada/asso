from fastapi import FastAPI
from state import State
from dto.DeviceDto import DeviceDto
from hubs.simulated_hub.hub import SimulatedHub

app = FastAPI()
state = State()

@app.get("/", status_code=202)
def read_root():
    return ""

@app.post("/device/")
def post_device(device_req: DeviceDto):
    return getattr(state.hubs["simulated"], device_req.inst)(device_req.device_path)

