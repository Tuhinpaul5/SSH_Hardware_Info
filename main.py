from fastapi import FastAPI
import uvicorn
from api.endpoints import router as cpu_router

app = FastAPI()

app.include_router(cpu_router, prefix="/get", tags=["cpu"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)