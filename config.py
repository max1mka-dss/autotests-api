from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import BaseModel,HttpUrl, FilePath


class HTTPClientConfig(BaseModel):
    url: HttpUrl

    timeout:float
    @property
    def client_url(self) -> str:
        return str(self.url)



class TestDataConfig(BaseModel):
    image_png_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="."

    )
    test_data: TestDataConfig
    http_client: HTTPClientConfig



#
# s = Settings(
#     test_data= TestDataConfig(image_png_file="./testdata/files/image.png"),
#     http_client=HTTPClientConfig(url="http://localhost:8000",timeout=100)
# )
# print(s.http_client.client_url)

settings = Settings()
#print(settings.http_client.client_url)