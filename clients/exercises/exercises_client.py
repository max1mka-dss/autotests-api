from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client,AuthenticationUserSchema

class Exercise(TypedDict):
    """
    Описание структуры упражнения
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExercisesResponseDict(TypedDict):
    exercises: list[Exercise]

class CreateExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа на создание упражнения
    """
    exercise: Exercise

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




class ExerciseClient(APIClient):
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка упражнений
        :param query: Словарь  с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)
    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercises_api(query)
        return response.json()


    def get_exercise_api(self,exercise_id:str) -> Response:
        """
        Метод получения упржажнения
        :param exercise_id: Идентификатор упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id :str ) -> GetExercisesResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания упражнения
        :param request:Словарь с title,courseId,maxScore,minScore,orderIndex,description,estimatedTime
        :return:   Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self,exercise_id:str, request: UpdateExerciseRequestDict ) -> Response:
        """
        Метод обновления упраженния
        :param exercise_id: Индентификатор упражнения
        :param request: Словарь с title,courseId,maxScore,minScore,orderIndex,description,estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch( f"/api/v1/exercises/{exercise_id}", json=request )
    def update_exercise(self,exercise_id: str,  request: UpdateExerciseRequestDict) ->CreateExercisesResponseDict:
        response = self.update_exercise_api(exercise_id,request)
        return response.json()
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

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExercisesResponseDict:
        """
        Метод преобразования ответа  от сервера в json формат для создания упражнений
        :param request:  данные для создания упражнения
        :return: ответ от сервера в json
        """
        response=self.create_exercise_api(request)
        return response.json()

def get_exercise_client(user: AuthenticationUserSchema) -> ExerciseClient:
    """
    Функция создает готовый экземпляяр ExerciseClient c уже настроенным клиентом.
    :return: Готовый к использованию ExerciseClient
    """
    return ExerciseClient(get_private_http_client(user))