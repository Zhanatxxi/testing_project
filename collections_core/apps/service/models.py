from sqlalchemy import (
    Column, Integer, String, 
    DateTime, Text, Boolean, ForeignKey
)
from sqlalchemy.orm import relationship

from apps.db.base import Model
from apps.service.utils import default_time


class Dispatch(Model):
    """ модель Рассылки для сервиса """

    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime)
    message = Column(Text)
    end_date = Column(DateTime)

    tag = Column(Boolean)

    message_id = Column(Integer, ForeignKey("message.id"))
    message = relationship("Parent", back_populates="dispatch")


class Message(Model):
    """ модель Сообщения для сервиса отправок  """

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=default_time)
    status = Column(Boolean, default=False)
    # dispatch_id = Column(Integer, ForeignKey("dispatch.id"))
    dispatch = relationship("Dispatch", back_populates="message")
    client = relationship("Client", back_populates="message")



    