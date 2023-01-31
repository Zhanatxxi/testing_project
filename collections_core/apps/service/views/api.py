from fastapi import APIRouter


router = APIRouter(prefix="/dispatch" ,tags=["Dispatch"])

@router.get("/")
async def service():
    return "Hello"




