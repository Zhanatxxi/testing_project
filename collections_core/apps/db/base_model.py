from inspect import isclass
from typing import Tuple, Union, List, Optional, Generator

from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import declared_attr

from collections_core.apps.db.constants import DEFAULT_PERMISSIONS



class ModelOptions:
    def __init__(
            self,
            model_name: str,
            table_name: str,
            verbose_name: Optional[str] = None,
            permissions: Optional[Union[List[List[str]], Tuple[Tuple]]] = None,
    ):
        self.model_name = model_name
        self.table_name = table_name
        self.verbose_name = verbose_name
        self.permissions = permissions or ()
        self.default_permissions = DEFAULT_PERMISSIONS


class BaseModelMeta(DeclarativeMeta):
    def __init__(cls, classname, bases, dict_, **kwargs):
        meta = getattr(cls, "Meta", None)
        options = ModelOptions(cls.__name__, cls.__tablename__)  # noqa
        if meta is not None and isclass(meta):
            options.verbose_name = getattr(meta, "verbose_name", cls.__name__)
            options.permissions = getattr(meta, "permissions", options.permissions)
        cls.options = options
        DeclarativeMeta.__init__(cls, classname, bases, dict_, **kwargs)


class BaseModel:
    @declared_attr
    def __tablename__(cls):  # noqa
        return cls.__name__.lower()

    @classmethod
    def child_generator(cls) -> Generator:
        for obj in Model.registry._class_registry.values():  # noqa
            if hasattr(obj, "__tablename__"):
                yield obj


Model = declarative_base(cls=BaseModel, metaclass=BaseModelMeta)