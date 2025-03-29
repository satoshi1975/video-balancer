from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Config
from app.redis_utils import get_cache, set_cache
from app.settings import settings
import re

async def redirect_logic(video: str, db: AsyncSession) -> str:
    #получениe конфигурации
    result = await db.execute(select(Config).limit(1))
    config = result.scalar_one_or_none()

    if not config:
        raise ValueError("Configuration not found")
    
    request_number_data = get_cache(settings.REQUEST_COUNTER_REDIS_KEY)
    
    if request_number_data:
        # Отправляем на оригинальный сервер
        if  request_number_data.get("number") + 1 == config.ratio:
            set_cache(settings.REQUEST_COUNTER_REDIS_KEY, {"number":0})
            return video
        
        else:
            # Отправляем на CDN
            match = re.search(r'//(s\d+)\.', video)
            if match:
                cluster = match.group(1)
            else:
                return None
            set_cache(settings.REQUEST_COUNTER_REDIS_KEY, {"number":request_number_data.get("number")+1})
            CDN_HOST = config.cdn_host if config.cdn_host else settings.CDN_HOST
            cdn_url = video.replace("s1.origin-cluster",f"{CDN_HOST}/{cluster}")
            return cdn_url
    else:
        set_cache(settings.REQUEST_COUNTER_REDIS_KEY, {"number":0})
        return video
