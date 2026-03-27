from db.migrate import run_migration
from sockets.server import start_server


def start():
    print("start")
    run_migration()
    print("migrate started")
    print("start server")
    start_server()
    print("started")
if __name__ == '__main__':
    start()