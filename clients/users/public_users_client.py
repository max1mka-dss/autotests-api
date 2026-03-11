from clients.api_client import APIClient
import httpx
from httpx import Response
from typing import TypedDict

from clients.public_http_builder import get_public_http_client
#from httpx_client import client

# Добавили описание структуры пользователя
class User(TypedDict):
    """
    Описание структуры пользователя.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


class CreateUserRequestDict (TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


# Добавили описание структуры ответа создания пользователя
class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа создания пользователя.
    """
    user: User


class PublicUsersClient(APIClient):
    def create_user_api(self,request: CreateUserRequestDict) -> Response:
        """
        Метод выполняет создание пользователя
        :param request: Словарь с email,password,lastName,firstName,middleName
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.post("/api/v1/users", json=request)

    def create_user(self,request: CreateUserRequestDict) -> CreateUserResponseDict:
        response = self.create_user_api(request)
        return response.json()

"""login_data: CreateUserRequestDict = {
    "email": "tes447@example.com",
    "password": "securepass123",
    "lastName": "Ivanov",
    "firstName": "Maksim",
    "middleName": "Ivanovich"
}
#http_client = httpx.Client(base_url = "http://localhost:8000/")
http_client = PublicUsersClient(client =client )
response = http_client.create_user_api(login_data)
print("Response from create user",response.json())"""

def get_public_users_client() -> PublicUsersClient:
    return PublicUsersClient(client=get_public_http_client())