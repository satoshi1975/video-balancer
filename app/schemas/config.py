from pydantic import BaseModel

class ConfigCreate(BaseModel):
    id: int
    cdn_host: str
    ratio: int
