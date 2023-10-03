from app.data.endpoints import router

def define_webpage_routes(app):
    app.include_router(router, prefix="/pages", tags=["webpage"])