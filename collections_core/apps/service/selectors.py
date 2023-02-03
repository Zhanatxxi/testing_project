from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from collections_core.apps.service.models import Message, Dispatch
from collections_core.apps.clients.models import User


async def get_all_messages(db: AsyncSession):
    query = select(Message.id, Message.created_at, Message.status)
    result = await db.execute(query)
    return result


async def get_test_message_rela_client(db: AsyncSession):
    query = select(Message.id, Message.created_at, Message.status, User).join(User.message)
    result = await db.execute(query)
    return result


async def get_all_dispatchers(db: AsyncSession):
    query = select(Dispatch.id, Dispatch.message, Dispatch.tag)
    result = await db.execute(query)
    return result


async def get_message_by_id(db: AsyncSession, *, message_id: int):
    query = select(Message).filter(Message.id == message_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()


async def get_dispatch_by_id(db: AsyncSession, *, dispatch_id: int):
    query = select(Dispatch).filter(Dispatch.id == dispatch_id)
    result = await db.execute(query)
    return result.scalar_one_or_none()
