from wsgiref.simple_server import make_server
from organs_framework.main import Framework
from views import routes

# Создаём объект WSGI - приложения
application = Framework(routes)

with make_server('', 8080, application) as httpd:
    print("Запуск на порту 8080...")
    print('http://127.0.0.1:8080/')
    httpd.serve_forever()
