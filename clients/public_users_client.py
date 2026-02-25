from clients.api_client import APIClient
import httpx
from httpx import Response
from typing import TypedDict
from httpx_client import client

class LoginRequestDict (TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    def create_user_api(self,request: LoginRequestDict) -> Response:
        """
        Метод выполняет создание пользователя
        :param request: Словарь с email,password,lastName,firstName,middleName
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.post("/api/v1/users", json=request)

# login_data: LoginRequestDict = {
#     "email": "tes447@example.com",
#     "password": "securepass123",
#     "lastName": "Ivanov",
#     "firstName": "Maksim",
#     "middleName": "Ivanovich"
# }
# #http_client = httpx.Client(base_url = "http://localhost:8000/")
# http_client = PublicUsersClient(client =client )
# response = http_client.create_user_api(login_data)
# print(response.json())