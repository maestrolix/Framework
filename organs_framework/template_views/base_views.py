from organs_framework.templater import render


class TemplateView:
    template_name = 'template.html'

    def get_context_data(self):
        return {}

    def get_template(self):
        return self.template_name

    def render_template_with_context(self, code='200 ok'):
        template_name = self.get_template()
        context = self.get_context_data()
        return code, render(template_name, **context)

    def __call__(self, request):
        return self.render_template_with_context()


class ListView(TemplateView):
    queryset = []
    template_name = 'list.html'
    context_object_name = 'objects_list'

    def get_queryset(self):
        print(self.queryset)
        return self.queryset

    def get_context_object_name(self):
        return self.context_object_name

    def get_context_data(self):
        queryset = self.get_queryset()
        context_object_name = self.get_context_object_name()
        context = {context_object_name: queryset}
        return context


class CreateView(TemplateView):
    template_name = 'create.html'

    @staticmethod
    def get_request_data(request):
        return request['data']

    @staticmethod
    def create_obj(data):
        pass

    def __call__(self, request):
        if request['method'] == 'POST':
            # метод поста
            data = self.get_request_data(request)
            self.create_obj(data)

            return self.render_template_with_context('201 CREATED')
        else:
            return super().__call__(request)
