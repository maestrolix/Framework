#!/usr/bin/env python
import sys


def main():
    try:
        from organs_framework.management import execute_command
    except ImportError as exc:
        raise ImportError(
            "Проверьте есть ли у вас доступ к фреймворку"
        ) from exc
    execute_command(sys.argv)


if __name__ == '__main__':
    main()
