import re


class AppRoute:
    def __init__(self, routes, url):
        self.routes = routes
        self.params = {}
        for p in re.findall(r'\w{3}:\w+', url):
            list_params = p.split(':')
            self.params[list_params[0]] = list_params[1]

        if len(self.params) != 0:
            for i in re.findall(r'<\w{3}:\w+>/', url):
                url = url.replace(i, '')
        self.url = url

    def __call__(self, cls):
        self.routes[self.url] = cls()
