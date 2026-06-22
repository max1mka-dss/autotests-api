from http import HTTPStatus

from tools.assertions.base import assert_equal
from clients.users.users_schema import UserSchema, GetUserResponseSchema, CreateUserResponseSchema
import allure
@allure.step("Check user")
def assert_user (actual: UserSchema, expected: UserSchema):
    """
    Проверяет, что фактические данные пользователя соответствуют ожидаемым.
    :param actual : Фактические данные пользователя.
    :param expected: Ожидаемые Данные пользователя.
    :return: Если хотя бы одно поле не совпадает
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")
@allure.step("Check get user response")
def assert_get_user_response (get_user_response: GetUserResponseSchema,create_user_response: CreateUserResponseSchema):

    assert_user(get_user_response.user, create_user_response.user)
@allure.step("Check create user response")
def assert_create_user_response (request: CreateUserResponseSchema, response: CreateUserResponseSchema):
    """
    Проверяет, чот ответ на создание пользователя соответствует запросу
    :param request: Исходный запрос на создание пользователя
    :param response: Ответ API с данными пользователя
    :raises Assertion Error: Если хотя бы одно поле не совпадает
    """
    assert_equal(response.user.email,request.email, "email")
    assert_equal(response.user.last_name,request.last_name, "last_name")
    assert_equal(response.user.first_name,request.first_name, "first_name")
    assert_equal(response.user.middle_name,request.middle_name, "middle_name")
