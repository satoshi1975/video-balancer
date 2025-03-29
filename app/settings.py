from pydantic_settings import BaseSettings
from pydantic import Field

class Setting(BaseSettings):
    CDN_HOST: str = Field(default="s1.origin-cluster", alias="CDN_HOST")
    REQUEST_COUNTER_REDIS_KEY: str = Field(default="request_number", alias="REQUEST_COUNTER_REDIS_KEY")


settings = Setting()