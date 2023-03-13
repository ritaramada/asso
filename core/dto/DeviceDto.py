from pydantic import BaseModel

class DeviceDto(BaseModel):
    inst: str
    device_path: str