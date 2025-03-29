from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db import get_db
from app.models import Config
from app.schemas.config import ConfigCreate

router = APIRouter()

@router.get("/")
async def get_config(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Config).limit(1))
    config = result.scalar_one_or_none()
    
    if not config:
        raise HTTPException(status_code=404, detail="Configuration not found")
    
    return {"cdn_host": config.cdn_host, "ratio": config.ratio}

@router.post("/", response_model = ConfigCreate)
async def create_config(config_data: ConfigCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Config).limit(1))
    config = result.scalar_one_or_none()
    if config:
        raise HTTPException(status_code=409, detail="Configuration already exist")
    config_data = config_data.model_dump(exclude_unset = True)
    config = Config(**config_data)
    db.add(config)
    await db.commit()

    if not config:
        raise HTTPException(status_code=404, detail="Configuration not found")
    
    return config_data

@router.put("/")
async def update_config(cdn_host: str, ratio: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Config).limit(1))
    config = result.scalar_one_or_none()
    
    if config:
        config.cdn_host = cdn_host
        config.ratio = ratio
    else:
        config = Config(cdn_host=cdn_host, ratio=ratio)
        db.add(config)
    
    await db.commit()
    return {"message": "Configuration updated"}
