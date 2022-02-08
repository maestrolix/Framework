import sqlite3
from organs_framework.exceptions import \
    RecordNotFoundException, \
    DbCommitException, \
    DbUpdateException, \
    DbDeleteException
from organs_framework.base_models import *


class UserMapper:
    """ ORM для пользователя """

    def __init__(self, connect):
        self.connection = connect
        self.cursor = connection.cursor()
        self.db_table = 'user'

    def all(self):
        statement = f'SELECT * FROM {self.db_table}'
        self.cursor.execute(statement)
        result = []
        for item in self.cursor.fetchall():
            id, name, password = item
            user = User(name, password)
            user.id = id
            result.append(user)
        return result

    def find_by_id(self, id):
        statement = f'SELECT * FROM {self.db_table} WHERE id=?'
        self.cursor.execute(statement, (id,))
        result = self.cursor.fetchone()
        if result:
            return User(**result)
        else:
            raise RecordNotFoundException(f'record with id={id} not found')

    def create(self, **kwargs):
        obj = User(**kwargs)
        statement = f'INSERT INTO {self.db_table} (name, password) VALUES (?, ?)'
        self.cursor.execute(statement, (obj.name, obj.password))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbCommitException(e.args)

    def update(self, obj):
        statement = f'UPDATE {self.db_table} SET name=? WHERE id=?'
        self.cursor.execute(statement, (obj.name, obj.id))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbUpdateException(e.args)

    def delete(self, obj):
        statement = f'DELETE FROM {self.db_table} WHERE id=?'
        self.cursor.execute(statement, (obj.id,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbDeleteException(e.args)


connection = sqlite3.connect('project.sqlite')


class MapperRegistry:
    mapper = {
        'user': UserMapper,
    }

    @staticmethod
    def get_current_mapper(name):
        # name = str(type(obj).__name__).lower()
        return MapperRegistry.mapper[name](connection)



