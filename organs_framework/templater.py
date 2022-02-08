from jinja2 import FileSystemLoader
from jinja2.environment import Environment


def render(template_name, folder='template', **kwargs):
    """
    :param template_name: имя шаблона
    :param folder: папка в которой ищем шаблон
    :param kwargs: параметры, передаваемые в шаблон
    :return: Рендерим шаблон с параметрами
    """
    env = Environment()
    env.loader = FileSystemLoader(folder)
    template = env.get_template(template_name)
    return template.render(**kwargs)
