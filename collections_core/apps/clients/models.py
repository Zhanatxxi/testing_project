from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from apps.db.base_model import Model
from apps.commons.phone_number import PhoneNumber


class User(Model):
    """SQLAlchemy декларативная описание таблицы пользователей"""

    class Meta:
        verbose_name = "Пользователь"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, info={
        "verbose_name": "Email пользователя"
    })

    _phone_number = Column(String(150), info={
        "verbose_name": "Номер телефона пользователя"
    })

    is_active = Column(Boolean(), default=False)

    message_id = Column(Integer, ForeignKey("message.id"))
    message = relationship("Parent", back_populates="dispatch")

    @hybrid_property
    def phone_number(self)-> PhoneNumber:
        """getter возвращает обьект класса PhoneNumber"""
        return PhoneNumber.from_string(self._phone_number, region="RU")


    @phone_number.expression
    def phone_number(cls) -> str:  # noqa
        return cls._phone_number
    
        