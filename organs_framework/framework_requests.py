from abc import ABC, abstractmethod


class AbstractRequest(ABC):

    def __init__(self, environ):
        self.environ = environ

    @staticmethod
    def parse_input_data(data: str) -> dict:
        # Делим параметры через &
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                # Делим ключ и значение через =
                key, value = item.split('=')
                result[key] = value
        return result

    @abstractmethod
    def get_request_params(self):
        pass


class GetRequest(AbstractRequest):

    def get_request_params(self):
        # Получаем параметры запроса
        data = self.environ['QUERY_STRING']
        return self.parse_input_data(data)


class PostRequest(AbstractRequest):

    def _get_wsgi_input(self) -> bytes:
        # Получаем длину тела
        content_length_data = self.environ.get('CONTENT_LENGTH')
        # Приводим к числовому значению
        content_length = int(content_length_data) if content_length_data else 0
        # Считываем данные, если они есть
        data = ''
        if content_length > 0:
            data = self.environ['wsgi.input'].read(content_length)
        else:
            data = b''
        return data

    def _parse_wsgi_input_data(self) -> dict:
        result = {}
        data = self._get_wsgi_input()
        if data:
            # Декодируем данные из байтов
            data_str = data.decode(encoding='utf-8')
            # Собираем их в словарь
            result = self.parse_input_data(data_str)

        return result

    def get_request_params(self) -> dict:
        return self._parse_wsgi_input_data()
