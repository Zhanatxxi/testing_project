from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from collections_core.apps.clients.models import User
from collections_core.apps.clients.schemas  import UserSchema


async def get_user_by_id(db: AsyncSession, user_id: int) -> User:
    query = select(User).filter(User.id==user_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()


async def create_client(db: AsyncSession, client: UserSchema) -> User:
    user = User(
        email=client.email,
        _phone_number=client.phone_number
    )
    db.add(user)
    db.commit()
    return user


