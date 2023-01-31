from sqlalchemy import (
    Column, Integer, String, 
    DateTime, Text, Boolean, ForeignKey
)
from sqlalchemy.orm import relationship

from collections_core.apps.db.base import Model
from collections_core.apps.service.utils import default_time


class Dispatch(Model):
    """ модель Рассылки для сервиса """

    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime)
    message = Column(Text)
    end_date = Column(DateTime)

    tag = Column(Boolean)

    message_ref = relationship("Message", backref="dispatch")
    message_id = Column(Integer, ForeignKey('message.id'), nullable=True )

    def __repr__(self) -> str:
        return "id:{} message: {} ---- tag:{}".format(
            self.id,
            self.message,
            self.tag
        )


class Message(Model):
    """ модель Сообщения для сервиса отправок  """

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=default_time)
    status = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return "{} {}".format(self.id, self.created_at)





    