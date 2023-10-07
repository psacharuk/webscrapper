import os
import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse

from app.model.webpage.routes import define_webpage_routes
from app.database.base import session_factory
from app.database.preparation import prepare_db

router = APIRouter()

def create_app():
    app = FastAPI(title="WebScrapper")
    define_webpage_routes(app)
    app.include_router(router, prefix="", tags=["welcome"])
    return app

fastapi_app = create_app()
session = session_factory(True)
prepare_db(session)

@fastapi_app.get("/", tags=["welcome"])
@router.get("/")
def welcome_page():
    return HTMLResponse(content=f"Welcome to WebScrapper. Go to <a href='/docs'>this link</a> to see the endpoints")

if __name__ == '__main__':
    uvicorn.run(fastapi_app, host=os.environ['SERVER_IP'], port=os.environ["FASTAPI_PORT"])