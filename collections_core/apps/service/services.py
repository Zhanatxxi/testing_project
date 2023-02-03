import aiohttp

from sqlalchemy.ext.asyncio import AsyncSession

from collections_core.config.config import settings
from collections_core.apps.service.schemas import (
    RemoteSendMessage, DispatchCreateSchema,
    MessageSchema
    )
from collections_core.apps.service.models import Dispatch, Message
from collections_core.apps.clients.selectors import get_user_by_id
from collections_core.apps.service.selectors import get_dispatch_by_id


async def send_message(*, msgid: int, data: RemoteSendMessage) -> int:
    """
    :msgid - id для удаленного сервера по рассылки
    :token - токен для удаленного сервер
    :data - тело запроса :RemoteSendMessage:
    :rtype: - статус код
    """
    SEND_URL = settings.PROBE_URL + f"v1/send/{msgid}"

    headers = {
        "Content-Type" : "application/json",
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDYxODMxMDYsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6Imh0dHBzOi8vdC5tZS9aaGFuYXR4eGkifQ.bfS32XVjHsK6Aa82qpNZHYDRv2UD_xSvcyHRY2Aj5MU'
        }

    async with aiohttp.ClientSession() as session:
        async with session.post(SEND_URL, headers=headers, data=data.json()) as response:
            return response


async def create_dispatcher(db: AsyncSession, dispatcher: DispatchCreateSchema):

    dispatch = Dispatch(
        start_date=dispatcher.start_date.replace(tzinfo=None),
        end_date=dispatcher.end_date.replace(tzinfo=None),
        message=dispatcher.message,
        tag=dispatcher.tag,
        message_id=dispatcher.message_id
    )
    db.add(dispatch)
    await db.commit()
    await db.refresh(dispatch)
    return dispatch


async def create_message(db: AsyncSession, message: MessageSchema):

    mes_instance = Message(
        created_at = message.created_at.replace(tzinfo=None),
        status = message.status
    )
    user_2 = await get_user_by_id(db, 2)
    mes_instance.user = [message.user_id, user_2]
    mes_instance.dispatch = [message.dispatch_id]

    db.add(mes_instance)
    await db.commit()
    await db.refresh(mes_instance)
    return mes_instance
