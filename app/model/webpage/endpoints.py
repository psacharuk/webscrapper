from app.database.connection import select_from_db
from app.model.webpage.schema import Webpage
from app.utils.webpage.page import get_page

from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/download/{url:path}")
def get_from_webpage(url):
    returned_url, content, error_info = get_page(url)
    if error_info:
        raise HTTPException(status_code=404, detail=error_info)
    return {"url": returned_url, "content": content}

@router.get("/db")
def get_from_db():
    return "data from db"

@router.get("/db/all")
def get_all_from_db():
    data_from_db = select_from_db(Webpage)
    if data_from_db == None:
        return "Still nothing in db"
    return data_from_db