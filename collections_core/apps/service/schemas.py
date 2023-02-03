from datetime import datetime

from pydantic import BaseModel
from collections_core.apps.clients.schemas import UserSchema


class RemoteSendMessage(BaseModel):
    id: int
    phone: int
    text: str


class MessageSchema(BaseModel):
    created_at: datetime
    status: bool
    dispatch_id: int
    user_id: int


class MessageWithUserSchema(MessageSchema):

    user: list[UserSchema]

    class Config:
        orm_mode = True


class DispatchShema(BaseModel):
    message: str
    tag: bool


class DispatchCreateSchema(DispatchShema):
    start_date: datetime
    end_date: datetime
    message_id: int


class DispatchOutSchema(DispatchCreateSchema):
    id: int
    