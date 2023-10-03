from fastapi import APIRouter

router = APIRouter()

@router.get("/from_webpage")
def get_from_webpage():
    return "data from webpage"

@router.get("/from_db")
def get_from_db():
    return "data from db"