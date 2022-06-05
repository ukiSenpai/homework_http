# У Яндекс.Диска есть очень удобное и простое API. Для описания всех его методов существует Полигон.
# Нужно написать программу, которая принимает на вход путь до файла на компьютере и сохраняет
# на Яндекс.Диск с таким же именем.
#
# Все ответы приходят в формате json;
# Загрузка файла по ссылке происходит с помощью метода put и передачи туда данных;
# Токен можно получить кликнув на полигоне на кнопку "Получить OAuth-токен".
# HOST: https://cloud-api.yandex.net:443

HOST = "https://cloud-api.yandex.net:443"
TOKEN = ""
UPLOAD_URL = "/v1/disk/resources/upload"

import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        headers = {
            'Authorization': self.token
        }
        params = {
            'path': file_path,
        }
        files = {
            'file': open(file_path, 'rb')
        }
        requests.put(requests.get(f"{HOST}{UPLOAD_URL}", headers=headers, params=params).json()['href'], files=files)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "test.txt"
    token = TOKEN
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
