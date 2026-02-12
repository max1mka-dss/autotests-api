import httpx

login_payload = {
  "email": "test@example.com",
  "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
# Выводим JSON-ответ и статус-код
print("Login reponse:" , login_response_data)
print("Status code:" , login_response.status_code)

#Payload для  обновления токена
refresh_payload = {
    "refreshToken": login_response_data["token"]["refreshToken"]
}

refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()

# Выводим обновленные токены
print("Refresh response:", refresh_response_data)
print("Status Code:", refresh_response.status_code)