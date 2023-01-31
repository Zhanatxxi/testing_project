from pydantic import BaseModel


class RemoteSendMessage(BaseModel):
    id: int
    phone: int
    text: str