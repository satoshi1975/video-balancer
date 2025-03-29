
from fastapi import FastAPI
from app.api.config import router as config_router
from app.api.balancer import router as balancer_router


app = FastAPI()


# Роут для API конфигурации
app.include_router(config_router, prefix="/config")
# Роут для API балансировки и редиректа
app.include_router(balancer_router, prefix="")

