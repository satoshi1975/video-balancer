from fastapi import APIRouter, Depends, HTTPException, Response
from app.services.balancer import redirect_logic
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.db import get_db

router = APIRouter()

@router.get("/")
async def redirect_video(video: str, db: Session = Depends(get_db)):
    if not video:
        raise HTTPException(status_code=400, detail="Video URL is required")
    
    redirect_url = await redirect_logic(video, db)
    if redirect_url:
        return RedirectResponse(url=redirect_url, status_code=301)
    
    raise HTTPException(status_code=400, detail="Incorrect cluster number in URL")
    
