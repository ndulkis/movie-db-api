
from fastapi import APIRouter


router = APIRouter( prefix =  "/movies") 



@router.get("/")
def movie_health_check():
    return {"status": "ok"}