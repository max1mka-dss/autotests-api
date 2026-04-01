from http import HTTPStatus

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginResponseSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema,CreateUserResponseSchema
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


def test_login():
    public_users_client = get_public_users_client()
    authentication_client =get_authentication_client()

    request = CreateUserRequestSchema()

    user_creation_response =public_users_client.create_user_api(request)
    #print(user_creation_response)
    user_creation_response_data = CreateUserResponseSchema.model_validate_json(user_creation_response.text)
    #print(user_creation_response_data)

    authentication_user = AuthenticationUserSchema(
        email=request.email,
        password=request.password
    )
    login_response = authentication_client.login_api(authentication_user)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)
    assert_status_code(login_response.status_code, HTTPStatus.OK)

    assert_login_response(login_response_data)

    validate_json_schema(login_response.json(), login_response_data.model_json_schema())