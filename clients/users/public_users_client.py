from clients.api_client import APIClient
from httpx import Response

from clients.public_http_builder import get_public_http_client
#from httpx_client import client
from clients.users.users_schema import UserSchema,CreateUserRequestSchema,CreateUserResponseSchema
import allure


class PublicUsersClient(APIClient):
    @allure.step("Create user")
    def create_user_api(self,request: CreateUserRequestSchema) -> Response:
        """
        Метод выполняет создание пользователя
        :param request: Словарь с email,password,lastName,firstName,middleName
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        return self.post("/api/v1/users", json=request.model_dump(by_alias=True))

    def create_user(self,request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)

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