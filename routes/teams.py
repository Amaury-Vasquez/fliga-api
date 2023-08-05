from fastapi import APIRouter

teams_router = APIRouter(
  prefix="/teams",
  tags=["teams"],
)

@teams_router.get("/")
def read_teams():
  return {"teams": []}


