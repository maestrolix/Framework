from organs_framework.framework_requests import PostRequest, GetRequest


class PageNotFound404:
    def __call__(self):
        return '404 NOT FOUND', 'Page not found'


class Framework:
    """ Данный класс - основа WSGI-фреймворка """

    def __init__(self, routes_obj):
        self.routes_list = routes_obj

    def __call__(self, environ, start_response):
        """ Получаем адрес, по которому пользователь выполнил переход """
        path = environ['PATH_INFO']

        # Получаем все данные из запроса
        request = {}
        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequest(environ).get_request_params()
            request['data'] = data
            print(f'Нам пришёл POST-запрос: {data}')
        if method == 'GET':
            requests_params = GetRequest(environ).get_request_params()
            request['request_params'] = requests_params
            print(f'Нам пришёл GET-запрос: {requests_params}')

        # Добавляем закрывающийся слеш, если нет
        if not path.endswith('/'):
            path = f'{path}/'

        # Находим нужный нам контроллер
        if path in self.routes_list:
            view = self.routes_list[path]
        else:
            view = PageNotFound404()

        # Запускаем контроллер
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data) -> dict:
        """
        Непонятно зачем мужик из статьи дважды декодировал данные,
        но на данный момент этот метод бессмысленный.
        Возможно это функция подстраховки с кириллицей
        """
        new_data = {}
        for key, value in data.items():
            val = bytes(value.replace('%', '=').replace("+", ' '), 'UTF-8')
            val_decode_str = val.decode('UTF-8')
            new_data[key] = val_decode_str
        return new_data
