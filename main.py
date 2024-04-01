from fastapi import FastAPI, APIRouter
from app.users.endpoints import router as user_router

app = FastAPI()

api_router = APIRouter()
api_router.include_router(user_router, prefix="/users", tags=["Users"])

app.include_router(api_router, prefix="/api/v1")

# @app.get("/api")
# async def root():
#     return {"message": "Hello World"}
