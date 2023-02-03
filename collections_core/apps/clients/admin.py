from sqladmin import  ModelView

from collections_core.apps.db.base import *


class UserAdmin(ModelView, model=User):
    column_list = (User.id, User.email, User._phone_number)
