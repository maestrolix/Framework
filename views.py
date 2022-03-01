from organs_framework.decorators import AppRoute
from models import Students
from organs_framework.db import Session
from organs_framework.base_views import ApiView, json_response

session = Session()

routes = {}


@AppRoute(routes=routes, url='/')
class Index(ApiView):
    def get(self, request):
        return '200 OK', 'Hello'


@AppRoute(routes=routes, url='/user-list/')
class UserList(ApiView):
    def get(self, request):
        users = session.query(Students).all()
        return json_response('200 OK', users)

    def post(self, request):
        title = request['data']['title']
        lastname = request['data']['lastname']
        session.add(Students(title=title, lastname=lastname))
        session.commit()
        return json_response('201 CREATED')


@AppRoute(routes=routes, url='/user-detail/<int:id>/')
class UserDetail(ApiView):
    def get(self, request):
        user_id = int(request['params']['id'])
        user = session.query(Students).get(user_id)
        return json_response('200 OK', user)
