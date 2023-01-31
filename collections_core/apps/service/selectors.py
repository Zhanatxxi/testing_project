import aiohttp

from collections_core.config.config import settings
from collections_core.apps.service.schemas import RemoteSendMessage


async def send_message(*, msgid: int, token: str, data: RemoteSendMessage) -> int:
    """
    :msgid - id для удаленного сервера по рассылки
    :token - токен для удаленного сервер
    :data - тело запроса :RemoteSendMessage:
    :rtype: - статус код
    """
    SEND_URL = settings.PROBE_URL + f"send/{msgid}"

    async with aiohttp.ClientSession() as session:
        async with session.get(SEND_URL) as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            return response.status

