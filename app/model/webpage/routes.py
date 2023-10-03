from app.model.webpage.endpoints import router

def define_webpage_routes(app):
    app.include_router(router, prefix="/webpages", tags=["webpage"])