import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.model.webpage.routes import define_webpage_routes
from app.database.base import session_factory
from app.database.preparation import prepare_db

def create_app():
    app = FastAPI(title="WebScrapper")
    define_webpage_routes(app)
    return app

fastapi_app = create_app()
session = session_factory(True)
prepare_db(session)

@fastapi_app.get("/")
def welcome_page():
    return HTMLResponse(content=f"Welcome to WebScrapper. Go to <a href='http://localhost:{os.environ['FASTAPI_PORT']}/docs'>this link</a> to see the endpoints")

if __name__ == '__main__':
    uvicorn.run(fastapi_app, host="0.0.0.0", port=os.environ["FASTAPI_PORT"])