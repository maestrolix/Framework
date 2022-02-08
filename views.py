from organs_framework.base_views import ListView, TemplateView, CreateView
from organs_framework.decorators import AppRoute
from organs_framework.orm import MapperRegistry

routes = {}


@AppRoute(routes=routes, url='/')
class Index(TemplateView):
    template_name = 'index.html'


@AppRoute(routes=routes, url='/about/')
class About:
    def __call__(self, request):
        return '200 OK', 'about'


@AppRoute(routes=routes, url='/registration/')
class Registration(CreateView):
    template_name = 'user-list.html'

    @staticmethod
    def create_obj(data):
        name = data['name']
        password = data['password']
        user_model = MapperRegistry.get_current_mapper('user')
        user_model.create(name=name, password=password)

    def get_context_data(self):
        return {'users': MapperRegistry.get_current_mapper('user').all()}


@AppRoute(routes=routes, url='/user-list/')
class UserList(ListView):
    queryset = MapperRegistry.get_current_mapper('user').all()
    template_name = 'user-list.html'
    context_object_name = 'users'
