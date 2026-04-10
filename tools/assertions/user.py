from http import HTTPStatus

from tools.assertions.base import assert_equal
from clients.users.users_schema import UserSchema


def assert_user (actual: UserSchema, expected: UserSchema):
    assert_equal(actual.user.id, expected.user.id, "id")
    assert_equal(actual.user.email, expected.user.email, "email")
    assert_equal(actual.user.last_name, expected.user.last_name, "last_name")
    assert_equal(actual.user.first_name, expected.user.first_name, "first_name")
    assert_equal(actual.user.middle_name, expected.user.middle_name, "middle_name")

def assert_get_user_response (get_user_response,create_user_response):
    assert_user(get_user_response, create_user_response)