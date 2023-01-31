from pydantic import BaseModel, EmailStr



class UserSchema(BaseModel):

    id: int
    email: EmailStr
    is_active: bool
    phone_number: str