# from venv import create

from db.connect import DBManager
from handlers.create_post import create_post
from handlers.delete_post import delete_post
from handlers.not_found import not_found
from handlers.post_list import post_list
from handlers.update_post import update_post


def handel_request(request:bytes) -> bytes:
    try:
        text = request.decode("utf-8", errors="ignore")
        line = text.split("\r\n", 1)[0]
        method, path, _ = line.split(" ")
        _, _, body = text.partition("\r\n\r\n")

    except Exception:
        return not_found()

    if method == "GET" and path == "/":
        return post_list()
    if method == "POST" and path == "/":
        return create_post(body)
    if path == "/delete":
        return delete_post(request.decode())
    if path == "/update":
        return update_post(request.decode())
    else:
        # print(not_found(request))
        return not_found()

