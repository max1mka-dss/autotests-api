from pydantic import BaseModel,ConfigDict,Field,EmailStr

class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class GetUserResponseSchema(BaseModel):
    """
    Описание структуры ответа получения пользователя.
    """
    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)
    email: EmailStr | None
    lastName: str | None
    firstName: str | None
    middleName: str | None


class UpdateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления пользователя.
    """
    user: UserSchema

class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    user: UserSchema
