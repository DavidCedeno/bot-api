from fastapi import APIRouter

health_router = APIRouter(prefix="/health")
    
@health_router.get("/live")
def check_live():
    return {"status": "alive"}

@health_router.get("/ready")
def check_ready():
    return {"status": "ready"}