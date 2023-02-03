from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from collections_core.apps.db.base_model import Model
from collections_core.apps.commons.phone_number import PhoneNumber


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

    message = relationship("Message", backref="user")
    message_id = Column(Integer, ForeignKey('message.id'), nullable=True)

    @hybrid_property
    def phone_number(self)-> PhoneNumber:
        """getter возвращает обьект класса PhoneNumber"""
        return PhoneNumber.from_string(self._phone_number, region="RU")

    @phone_number.expression
    def phone_number(cls) -> str:  # noqa
        return cls._phone_number

    @phone_number.setter
    def phone_number(self, value: str | PhoneNumber) -> None:
        """
        :param value: Принимает значение с типом строка или обьект класса PhoneNumber
        :return: setter ничег не возвращает
        """
        if isinstance(value, PhoneNumber):
            value = value.as_e164()
        self._phone_number = value
    
    def __repr__(self) -> str:
        return "id:{} email:{} is_active:{}".format(
            self.id,
            self.email,
            self.is_active
        )