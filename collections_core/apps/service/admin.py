from sqladmin import  ModelView

from collections_core.apps.service.models import Dispatch, Message


class DispatcherAdmin(ModelView, model=Dispatch):
    column_list = (
        Dispatch.id, Dispatch.start_date, 
        Dispatch.message, Dispatch.end_date,
        Dispatch.tag
        )


class MessageAdmin(ModelView, model=Message):
    column_list = (
        Message.id,
        Message.status
    )