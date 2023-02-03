from fastapi import APIRouter
from aiohttp.client_reqrep import ClientResponse

from collections_core.apps.service.schemas import RemoteSendMessage
from collections_core.apps.service.services import send_message


router = APIRouter(prefix="/remote_server" ,tags=["Send message"])


@router.post("/{msgid}")
async def service(msgid: int, data: RemoteSendMessage):
    response: ClientResponse = await send_message(
        msgid=msgid,
        data=data
    )
    return response.status