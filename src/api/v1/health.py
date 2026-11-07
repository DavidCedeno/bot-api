from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from src.dependencies import get_db

health_router = APIRouter(prefix="/health")
    
@health_router.get("/live")
def check_live():
    return {"status": "alive"}

@health_router.get("/ready")
def check_ready():
    return {"status": "ready"}

@health_router.get("/db-check")
def db_check(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1"))
    return {"result": result.scalar()}