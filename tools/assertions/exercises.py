
from clients.exercises.exercises_schema import CreateExerciseRequestSchema,CreateExercisesResponseSchema
from tools.assertions.base import assert_equal
def assert_create_exercise_response(
        request: CreateExerciseRequestSchema,
        response:CreateExercisesResponseSchema
):
    """
    Проверяет, что ответ на создание курса соответствует запросу на его создание
    :param CreateExerciseRequestSchema: Запрос на создание упражнения
    :param CreateExercisesResponseSchema: Ответ от сервера на запрос создания упражнения
    :return:
    """
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.course_id, request.course_id, "course_id")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.title, request.title, "title")


