from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client,AuthenticationUserSchema
from clients.exercises.exercises_schema import ExerciseSchema, GetExercisesResponseSchema, GetExercisesQuerySchema, \
    UpdateExerciseRequestSchema, CreateExercisesResponseSchema, CreateExerciseRequestSchema, GetExerciseResponseSchema
import allure

class ExerciseClient(APIClient):
    @allure.step("Get exercises")
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод получения списка упражнений
        :param query: Словарь  с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))
    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    @allure.step("Get exercise by id {exercise_id}")
    def get_exercise_api(self,exercise_id:str) -> Response:
        """
        Метод получения упржажнения
        :param exercise_id: Идентификатор упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id :str ) -> GetExerciseResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    @allure.step("Create exercise")
    def create_exercise_api(self, request: GetExercisesQuerySchema) -> Response:
        """
        Метод создания упражнения
        :param request:Словарь с title,courseId,maxScore,minScore,orderIndex,description,estimatedTime
        :return:   Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    @allure.step("Update exercise by id {exercise_id}")
    def update_exercise_api(self,exercise_id:str, request: UpdateExerciseRequestSchema ) -> Response:
        """
        Метод обновления упраженния
        :param exercise_id: Индентификатор упражнения
        :param request: Словарь с title,courseId,maxScore,minScore,orderIndex,description,estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch( f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True) )
    def update_exercise(self,exercise_id: str,  request: UpdateExerciseRequestSchema) ->CreateExercisesResponseSchema:
        response = self.update_exercise_api(exercise_id,request)
        return CreateExercisesResponseSchema.model_validate_json(response.text)

    @allure.step("Delete exercise by id {exercise_id}")
    def delete_exercise_api(self, exercise_id:str) -> Response:
        """
        Метод удаления упражнения
        :param exercise_id: Идентификатор упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")
    def delete_exercise(self,exercise_id:str) -> Response:
        response = self.delete_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExercisesResponseSchema:
        """
        Метод преобразования ответа  от сервера в json формат для создания упражнений
        :param request:  данные для создания упражнения
        :return: ответ от сервера в json
        """
        response=self.create_exercise_api(request)
        return CreateExercisesResponseSchema.model_validate_json(response.text)

def get_exercise_client(user: AuthenticationUserSchema) -> ExerciseClient:
    """
    Функция создает готовый экземпляяр ExerciseClient c уже настроенным клиентом.
    :return: Готовый к использованию ExerciseClient
    """
    return ExerciseClient(get_private_http_client(user))