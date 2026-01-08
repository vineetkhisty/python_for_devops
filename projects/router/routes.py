from service.devops_utils import get_system_status
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/metrics")

def get_metrics():

    try:
        metrics = get_system_status()

        return metrics
    except:
        raise HTTPException(
            status_code= 500,
            details= "Internal Server Error"
        )