from typing import TypedDict
from httpx import Response

class GetExercisesQueryDict (TypedDict):
    """
    Описание структуры запроса на получение списка упражнений
    """
    courseId: str
class CreateExerciseRequestDict(TypedDict):
        title: str
        courseId: str
        maxScore: int
        minScore: int
        orderIndex: int
        description: str
        estimatedTime: str
class UpdateExerciseRequestDict(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

from clients.api_client import APIClient


class ExerciseClient(APIClient):
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка упражнений
        :param query: Словарь  с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)
    def get_exercise_api(self,exercise_id:str) -> Response:
        """
        Метод получения упржажнения
        :param exercise_id: Идентификатор упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise(self, request: CreateExerciseRequestDict) -> Response
        """
        Метод создания упражнения
        :param request:Словарь с title,courseId,maxScore,minScore,orderIndex,description,estimatedTime
        :return:   Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)
    def update_exercise(self,exercise_id:str, request: UpdateExerciseRequestDict ) -> Response:
        """
        Метод обновления упраженния
        :param exercise_id: Индентификатор упражнения
        :param request: Словарь с title,courseId,maxScore,minScore,orderIndex,description,estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch( f"/api/v1/exercises/{exercise_id}", json=request )
    def delete_exercise(self, exercise_id:str) -> Response:
        """
        Метод удаления упражнения
        :param exercise_id: Идентификатор упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """