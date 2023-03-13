from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_led import GroveLed
from fastapi import FastAPI
from pydantic import BaseModel

CounterFitConnection.init('127.0.0.1', 5000)

app = FastAPI()
led = GroveLed(0) # ATTENTION: Pin is defined by default to 0

class LightState(BaseModel):
    state: bool

@app.get("/")
def read_root():
    return { 
        "type": "light"
    }

@app.post("/light/")
def control_light(data: LightState):
    if (data.state):
        led.on()
    else:
        led.off()
    return { "outcome": "ok" }
