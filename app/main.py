from fastapi import FastAPI
import uvicorn

def create_app():
    app = FastAPI(title="WebScrapper")
    return app

fastapi_app = create_app()

if __name__ == '__main__':
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)