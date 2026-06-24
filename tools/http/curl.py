"""
curl -X 'PATCH' \
  'http://localhost:8000/api/v1/users/b27e09b3-e667-49e6-a883-9a6c1a528258' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHBpcmUiOiIyMDI2LTA2LTIzVDEzOjI3OjUxLjQ5MDgxMSIsInVzZXJfaWQiOiJiMjdlMDliMy1lNjY3LTQ5ZTYtYTg4My05YTZjMWE1MjgyNTgifQ.ecBqUGGdjppI5jiZfMeNT3BK03VK4YS56me8aC5MUS0' \
  -H 'Content-Type: application/json' \
  -d '{
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}'
"""

from httpx import Request,RequestNotRead,post,Client
def make_curl_from_request(request: Request) -> str:

    """
    Генеририует команду cURL из HTTP-запроса httpx
    :param request:  HTTP запрос , из которого будет сформирована команда cURL
    :return:  Строка с командой cURL, содержащая метод запроса,URL, заголовки и тело(если есть)
    """
    result: list[str] = [f"curl -X '{request.method}'", f"'{request.url}'"]

    for header, value in request.headers.items():
        result.append(f"-H '{header}: {value}'")

    try:
        if body := request.content:
            result.append(f"-d '{body.decode('utf-8')}'")

    except RequestNotRead:
        pass

    return "\\\n ".join(result)

# body ={
#   "user": {
#     "id": "b27e09b3-e667-49e6-a883-9a6c1a528258",
#     "email": "test@example.com",
#     "lastName": "string",
#     "firstName": "string",
#     "middleName": "string"
#   }
# }
# response = post('http://localhost:8000/api/v1/users/',json = body)
# print(make_curl_from_request(response.request))
def print_request(request: Request):
    print(f"Выполняем запрос {request.method}")

#client= Client(event_hooks={"request": [print_request]} )
# client.get("http://localhost:8000/api/v1/users/")
# client.post("http://localhost:8000/api/v1/users/")
# client.patch("http://localhost:8000/api/v1/users/")
# client.delete("http://localhost:8000/api/v1/users/")