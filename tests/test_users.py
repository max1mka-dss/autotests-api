from http import HTTPStatus

from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.assert_create_user_response import assert_create_user_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema

def test_create_user():
    # Инициализируем API-клиент для работы с пользователями
    public_users_client = get_public_users_client()

    # Формируем тело запроса на создание пользователя
    request = CreateUserRequestSchema()
    # Отправляем запрос на создание пользователя
    response = public_users_client.create_user_api(request)
    #print("Response: ", response)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)
    #print("Response json", response.json())
    #print("Response pydantic model", response_data)

    # Проверяем статус-код ответа
    assert_status_code(response.status_code, HTTPStatus.OK)

    assert_create_user_response(request, response_data)

    validate_json_schema(response.json(), response_data.model_json_schema())