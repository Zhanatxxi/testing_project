from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession

from collections_core.apps.db.deps import get_db_session
from collections_core.apps.clients.schemas import UserSchema, UserCreateSchema
from collections_core.apps.clients import selectors


router = APIRouter(prefix="/client", tags=["Client"])


@router.get("/{user_id}", response_model=UserSchema)
async def get_user(
    user_id: int, 
    db: AsyncSession = Depends(get_db_session)
    ):
    """
    :user_id - this is interger id client in db
    return client object with not full information
    """
    
    user = await selectors.get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="not found is user_id"
        )

    return user.__dict__


@router.post("/create/")
async def create_client(
    client: UserCreateSchema,
    db: AsyncSession = Depends(get_db_session)
):
    user = await selectors.create_client(db, client)
 
    return user.__dict__


@router.get("/get/all", response_model=list[UserSchema])
async def get_all_clients(db: AsyncSession = Depends(get_db_session)):
    all_users = await selectors.all_clients(db)
    
    return [UserSchema(**user) for user in all_users]


