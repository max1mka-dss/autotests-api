
from clients.exercises.exercises_client import get_exercise_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExercisesResponseSchema
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture
from clients.exercises.exercises_client import ExerciseClient
import pytest
from pydantic import BaseModel

class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExercisesResponseSchema


@pytest.fixture
def exercises_client (function_user: UserFixture) -> ExerciseClient:
    return get_exercise_client (function_user.authentication_user)

@pytest.fixture
def function_exercise(
        exercises_client: ExerciseClient,
        function_course: CourseFixture
) -> ExerciseFixture:
    request = CreateExerciseRequestSchema( courseId=function_course.response.course.id)
    response = exercises_client.create_exercise(request)
    return ExerciseFixture (request=request, response=response)