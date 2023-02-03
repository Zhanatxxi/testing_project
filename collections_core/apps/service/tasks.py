from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from collections_core.apps.service.selectors import get_dispatch_by_id, get_message_by_id
from collections_core.apps.service.models import Message, Dispatch
from collections_core.apps.clients.models import User
from collections_core.apps.service.services import send_message
from collections_core.apps.service.schemas import RemoteSendMessage


async def test_task(message_id: int, message: str, db: AsyncSession):

    query = select(User.phone_number).where(Message.id == message_id).join(User.message)
    result = await db.execute(query)

    all_status = list()

    for user in result:
        phone = user[0]
        data = RemoteSendMessage(
            id=1,
            phone=phone,
            text=message
        )
  
        response = await send_message(msgid=1, data=data)
        all_status.append(response.status)

    print(all_status)
