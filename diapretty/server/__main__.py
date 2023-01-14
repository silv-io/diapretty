from werkzeug import run_simple

from diapretty.server.api import DiagnoseServer


def main():
    server = DiagnoseServer()
    run_simple("localhost", 4567, server.wsgi)


if __name__ == '__main__':
    main()
