import json


class ApiView:

    def get(self, request):
        pass

    def post(self, request):
        pass

    def delete(self, request):
        pass

    def update(self, request):
        pass

    def __call__(self, request):
        if request['method'] == 'GET':
            return self.get(request)
        elif request['method'] == 'POST':
            return self.post(request)
        elif request['method'] == 'DELETE':
            return self.delete(request)
        elif request['method'] == 'UPDATE':
            return self.update(request)


def json_response(code, data=None):
    if type(data) == list:
        serialize_data = [i.serialize for i in data]
        return code, str(json.dumps(serialize_data))
    elif data is None:
        return code, ''
    else:
        serialize_data = data.serialize
        return code, str(json.dumps(serialize_data))
