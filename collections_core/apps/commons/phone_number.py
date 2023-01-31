from typing import Optional, Union

from phonenumbers import (
    PhoneNumber as BasePhoneNumber,
    PhoneNumberFormat,
    parse as phone_number_parse,
    format_number,
    is_valid_number
)
from phonenumbers.phonenumberutil import NumberParseException

from config.config import settings


class PhoneNumber(BasePhoneNumber):
    """Тип для работы с номерами телефонами"""

    #: Константа форматов для display
    class Formats:
        E164 = PhoneNumberFormat.E164
        INTERNATIONAL = PhoneNumberFormat.INTERNATIONAL
        NATIONAL = PhoneNumberFormat.NATIONAL

    def as_e164(self):
        """Возвращает строку в формате `+77751347714`"""
        return format_number(self, self.Formats.E164)

    def as_international(self):
        """Возвращает строку в формате `+7 775 134 7714`"""
        return format_number(self, self.Formats.INTERNATIONAL)

    def as_national(self):
        """Возвращает строку в формате `8 (775) 134 7714`"""
        return format_number(self, self.Formats.NATIONAL)

    def as_msisdn(self):
        """Возвращает строку в формате `77751347714`"""
        return f"{self.country_code}{self.national_number}"

    @classmethod
    def from_string(
            cls,
            phone_number: str,
            region: Optional[str] = settings.PHONE_NUMBER_REGION
    ):
        """Классметод создает из взодящего параметра класс :class:`.PhoneNumber`
        :type phone_number: Номер телефона с типом строка
        :type region: Не обязательный параметр с значением по умолчанию `KZ`.
        Значение по умолчанию меняется в в :class:`collections_core.config.config.settings.PHONE_NUMBER_REGION`
        :return: Возвращает класс :class:`.PhoneNumber`
        """
        new_cls = cls()
        phone_number_parse(
            phone_number,
            region=region,
            numobj=new_cls
        )
        return new_cls

    @classmethod
    def __get_validators__(cls):
        """Валидаторы для входящих параметров из дочерных классаов
        модели :class:`pydantic.BaseModel`"""
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema):
        """Модифицируем схему OpenApi(Swagger)"""
        field_schema.update(
            pattenr=r"^\+(7)(77[0-9])([0-9]{7})",
            examples="+77777777777",
            type="str"
        )

    @classmethod
    def validate(cls, v: Union[str, "PhoneNumber"]) -> Union[str, "PhoneNumber"]:
        """Принимает во вход строку или обьект класса :class:`.PhoneNumber`.
        Если строка валидирует номер телефона и возвращает :class:`.PhoneNumber`.
        Если обьект класса :class:`.PhoneNumber`, то возвращает строку str(v) """

        text = "Не валидный номер телефона"
        if isinstance(v, cls):
            return str(v)
        try:
            phone_number = cls.from_string(v)
        except NumberParseException:
            raise ValueError(text)
        if not is_valid_number(phone_number):
            raise ValueError(text)
        return phone_number

    def __str__(self):
        return self.as_e164()

    def __len__(self):
        return len(str(self))

    def display(self) -> str:
        return str(self)