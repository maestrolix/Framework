
def execute_command(argv=None):
    command = argv[1]
    print(command)
    if command == 'runserver':
        from organs_framework import run
        return run
    elif command == 'create-db':
        from organs_framework import create_db
        return create_db
