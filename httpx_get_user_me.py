
import httpx
login_payload = {
  "email": "test@example.com",
  "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
# Выводим  статус-код и JSON-ответ
print("Status code:" , login_response.status_code)
print("Login response:" , login_response_data)
#print("Access Token:" , login_response_data["token"]["accessToken"])

# Формируем строку с токеном для подстановки в headers
auth_token ="Bearer "+ login_response_data["token"]["accessToken"]
# Определяем переменную headers  
headers = {"Authorization": auth_token }
response_users_me = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
print("Status code:" , response_users_me.status_code)
response_me_data = response_users_me.json()
print("Response me data is", response_me_data)