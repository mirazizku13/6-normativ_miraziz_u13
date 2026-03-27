from urllib.parse import parse_qs
from db.connect import DBManager
from handlers.post_list import post_list
from units.http import response

#
# # def delete_post(request):
# #     request = request.decode()  # 🔥 SHU QATORNI QO‘SH
# #
# #     body = request.split("\r\n\r\n")[-1]
# #     post_id = body.split("=")[-1]
# #
# #     with DBManager() as cur:
# #         cur.execute("DELETE FROM postings WHERE id = %s", (post_id,))
# #
# #     return post_list()
#
# def delete_post(request):
#     id = request.GET.get("id")
#
#     with DBManager() as cur:
#         cur.execute("DELETE FROM postings WHERE id = %s", (id,))
#
#     return post_list()
#
# def delete_post(request):
#     return response("Delete page")

def delete_post(request):
    # request ni stringga o‘tkazish
    request = request.decode()

    # URLni olish
    first_line = request.split("\n")[0]  # GET /delete?id=1 HTTP/1.1
    path = first_line.split(" ")[1]      # /delete?id=1

    # IDni ajratish
    if "?" in path:
        query = path.split("?")[1]       # id=1
        params = dict(q.split("=") for q in query.split("&"))
        id = params.get("id")
    else:
        id = None

    # DB dan o‘chirish
    with DBManager() as cur:
        cur.execute("DELETE FROM postings WHERE id = %s", (id,))

    # post_list sahifaga qaytarish
    return post_list()   # post_list() html qaytaradigan funksiya