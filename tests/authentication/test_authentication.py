from http import HTTPStatus
import pytest
from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient
from clients.authentication.authentication_schema import LoginResponseSchema, LoginRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema,CreateUserResponseSchema
from fixtures.users import UserFixture
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.allure.tags import AllureTag
import allure

@pytest.mark.authentication  # Добавили маркировку users
@pytest.mark.regression  # Добавили маркировку regression
@allure.tag (AllureTag.REGRESSION,AllureTag.AUTHENTICATION)
class TestAuthentication:
    @allure.title("Login with correct email and password")
    def test_login(self, function_user: UserFixture, authentication_client: AuthenticationClient):
        # print(user_creation_response)

        authentication_user = LoginRequestSchema(email=function_user.email, password=function_user.password)
        response = authentication_client.login_api(authentication_user)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_response(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())
