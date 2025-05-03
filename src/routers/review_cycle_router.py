from fastapi import APIRouter, HTTPException
from src.models.review_cycle import ReviewCycle
from src.services.review_cycle_service import ReviewCycleService
from src.repositories.review_cycle_repository import ReviewCycleRepository

router = APIRouter()
service = ReviewCycleService(ReviewCycleRepository())

@router.post("/")
def start_cycle(cycle_id: str, reviewer_id: str, description: str):
    try:
        service.start_cycle(cycle_id, reviewer_id, description)
        return {"message": "Cycle started successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{cycle_id}/complete")
def complete_cycle(cycle_id: str):
    try:
        service.complete_cycle(cycle_id)
        return {"message": "Cycle completed"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/active")
def list_active_cycles():
    return service.list_active_cycles()

@router.get("/")
def list_all_cycles():
    return service.repository.list_all()
