from handlers.post_list import post_list
from db.connect import DBManager

from urllib.parse import parse_qs

from units.http import response


#
#
# def update_post(request):
#     body = request.split("\r\n\r\n")[-1]
#     data = parse_qs(body)
#
#     title = data.get("title", [""])[0]
#     content = data.get("content", [""])[0]
#     post_id = data.get("id", [""])[0]
#
#     with DBManager() as cur:
#         cur.execute(
#             "UPDATE postings SET title=%s, content=%s WHERE id=%s",
#             (title, content, post_id)
#         )
#
#     return post_list()

def update_post(request):
    body = "<h1>Update Page</h1>"
    return response(body)