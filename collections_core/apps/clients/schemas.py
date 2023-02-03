from pydantic import BaseModel, EmailStr, Field



class UserSchema(BaseModel):

    id: int
    email: EmailStr
    is_active: bool
    # phone_number: str


class UserCreateSchema(BaseModel):
    email: EmailStr
    phone_number: str
    is_active: bool = Field(default=True)

