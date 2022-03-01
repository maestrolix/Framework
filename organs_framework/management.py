
def execute_command(argv=None):
    command = argv[1]
    if command == 'runserver':
        from organs_framework import run
        return run
    elif command == 'create-db':
        from organs_framework import db
        return db
