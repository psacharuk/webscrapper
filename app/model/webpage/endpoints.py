from app.database.connection import select_from_db, insert_into_db, update_db, delete_from_db
from app.model.webpage.schema import Webpage
from app.utils.webpage.page import get_page
from app.utils.webpage.parser import parse_content

from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/download/{url:path}")
def get_from_webpage(url):
    returned_url, content, error_info = get_page(url)
    if error_info or content is None:
        raise HTTPException(status_code=404, detail=error_info)
    head, body, footer = parse_content(content)
    webpage = Webpage(address=returned_url, head=head, body=body, foot=footer)
    try:
        # ADDRESS is unique so check if element exists. If yes then should be updated
        get_from_db(returned_url)
        update_db(webpage, {'head': head, 'body': body, 'foot': footer})
    except HTTPException:
        # if element do not exist insert it in db
        insert_into_db(webpage)

    return {"address": returned_url, "content": {
        "head": head,
        "body": body,
        "foot": footer
    }}

@router.get("/db/{url:path}")
def get_from_db(url):
    webpages = get_all_from_db()
    for page in webpages:
        if page.address == url:
            return page
    raise HTTPException(status_code=404, detail="Not found")


@router.get("/db-all")
def get_all_from_db():
    return select_from_db(Webpage)


@router.delete('/db/{url:path}')
def remove_from_db(url):
    object_to_remove = get_from_db(url)
    delete_from_db(object_to_remove)
    return f"Object with {url} removed"