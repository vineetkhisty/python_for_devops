from service.devops_utils import get_system_status
from service.aws_utils import get_bucket_info
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
    
@router.get("/s3")
def get_bucket():
    try:
       get_bucket_info()

    #    return bucket
    except:
        raise HTTPException(
            status_code= 500,
            details= "Internal Server Error"
        )