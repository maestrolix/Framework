#  DataBase Exceptions start
class RecordNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(f'Record not found: {message}')


class DbCommitException(Exception):
    def __init__(self, message):
        super().__init__(f'Db commit exception: {message}')


class DbUpdateException(Exception):
    def __init__(self, message):
        super().__init__(f'Db update exception: {message}')


class DbDeleteException(Exception):
    def __init__(self, message):
        super().__init__(f'Db delete exception: {message}')
