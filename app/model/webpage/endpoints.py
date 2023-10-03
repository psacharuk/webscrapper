from app.database.connection import select_from_db
from app.model.webpage.schema import Webpage

from fastapi import APIRouter

router = APIRouter()

@router.get("/download")
def get_from_webpage():
    return "data from internet"

@router.get("/db")
def get_from_db():
    return "data from db"

@router.get("/db/all")
def get_all_from_db():
    data_from_db = select_from_db(Webpage)
    if data_from_db == None:
        return "Still nothing in db"
    return data_from_db