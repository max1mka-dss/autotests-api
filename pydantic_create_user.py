from pydantic import BaseModel, Field,EmailStr
import uuid

class UserDefaultSchema(BaseModel):
    """
    Базовая модель, от которой будут наследоваться модели для создания и ответов
    """
    email: EmailStr
    last_name: str = Field(alias="lastName"),
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class UserSchema(UserDefaultSchema):
    """"
    Модель описывает структура объекта пользователя
    """
    id:  str = Field(default_factory=lambda: str(uuid.uuid4()))

class CreateUserRequestSchema(UserDefaultSchema):
    """
    Модель описывает структуру запроса для создания пользователя
    """
    password: str


class CreateUserResponseSchema(BaseModel):
    """
    Модель описыает структура ответа запроса создания пользователя
    """
    user: UserSchema


