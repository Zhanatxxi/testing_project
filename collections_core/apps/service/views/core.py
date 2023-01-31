from fastapi import APIRouter

from collections_core.apps.service.schemas import RemoteSendMessage
from collections_core.apps.service.selectors import send_message


router = APIRouter(prefix="/remote_server" ,tags=["Send message"])


@router.get("/{msgid}")
async def service(msgid: int, data: RemoteSendMessage):
    response_status = await send_message(
        msgid=1,
        token="adasdasd2332asd",
        data=data
    )
    return response_status