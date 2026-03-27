from urllib.parse import parse_qs

from db.connect import DBManager
from handlers.post_list import post_list


def create_post(body):
    data = parse_qs(body)
    title = data.get("title", [""])[0]
    content = data.get("content", [""])[0]

    with DBManager() as cur:
        cur.execute("INSERT INTO postings (title, content) VALUES (%s, %s)", (title, content))

    return post_list()