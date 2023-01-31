from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession

from collections_core.apps.db.deps import get_db_session
from collections_core.apps.clients.schemas import UserSchema
from collections_core.apps.clients import selectors


router = APIRouter(prefix="/client" ,tags=["Client"])


@router.get("/{user_id}", response_model=UserSchema)
async def get_user(
    user_id: int, 
    db: AsyncSession = Depends(get_db_session)
    ) -> UserSchema:
    
    user = await selectors.get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="not found is user_id"
        )
    
    return user


@router.post("/create/", response_model=UserSchema)
async def create_client(
    client: UserSchema,
    db: AsyncSession = Depends(get_db_session)
):
    user = await selectors.create_client(db, client)
    return user


