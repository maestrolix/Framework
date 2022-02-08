from abc import ABC
import quopri


class BaseUser(ABC):

    def __init__(self, name, password):
        self.id = ''
        self.name = name
        self.password = password

    def __str__(self):
        return self.name


class Admin(BaseUser):
    pass


class User(BaseUser):
    pass


class UserFactory:
    """ Класс-Фабрика пользователей """
    types = {
        'admin': Admin,
        'user': User
    }

    @classmethod
    def create(cls, type_, username, password):
        return cls.types[type_](username, password)


class BaseGroup(ABC):

    def __init__(self, title):
        self.admin = []
        self.title = title


class PublicPostGroup(BaseGroup):
    """ Публицисты внутри в админ панели """
    pass


class TestGroup(BaseGroup):
    """ Тестировщики """
    pass


class GroupFactory:
    """ Класс-Фабрика групп администрации """
    types = {
        'public_post_group': PublicPostGroup,
        'test_group': TestGroup
    }

    @classmethod
    def create(cls, type_, title):
        return cls.types[type_](title)


# class Engine:
#     """ Класс-Основной интерфейс проекта """
#
#     def __init__(self):
#         self.users = []
#         self.admins = []
#         self.test_groups = []
#         self.publish_groups = []
#
#     def create(self, type_, name, password):
#         new_user = UserFactory.create(type_, name, password)
#         self.users.append(new_user)
#         return self.users
#
#     def find_user_by_id(self, user_id):
#         for user in self.users:
#             print('item', user.id)
#             if user.id == user_id:
#                 return user
#         raise Exception(f'Нет пользователя с id = {user_id}')
#
#     @staticmethod
#     def create_group(type_, title):
#         return GroupFactory.create(type_, title)
#
#     def get_group(self, title):
#         for group in self.test_groups:
#             if group.title == title:
#                 return group
#         return None
#
#     @staticmethod
#     def decode_value(val):
#         val_b = bytes(val.replace('%', '=').replace("+", " "), 'UTF-8')
#         val_decode_str = quopri.decodestring(val_b)
#         return val_decode_str.decode('UTF-8')
