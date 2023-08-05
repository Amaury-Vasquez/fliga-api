from fastapi import APIRouter
from routes.teams import teams_router
from routes.auth import auth_router

app_router = APIRouter(
  prefix="/api",
  responses={404: {"description": "Not found"}}
)

app_router.include_router(teams_router)
app_router.include_router(auth_router)