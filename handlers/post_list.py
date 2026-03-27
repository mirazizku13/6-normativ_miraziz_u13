# from db.connect import DBManager
# from units.http import response
#
#
# def post_list():
#     with DBManager() as cur:
#         cur.execute(
#             """SELECT * FROM postings"""
#         )
#         posts = cur.fetchall()
#     body = """
#            <!DOCTYPE html>
#            <html>
#                <head>
#                    <title>Posts</title>
#                    <style>
#                        body {
#                            font-family: Arial, sans-serif;
#                            background-color: #f4f6f8;
#                            margin: 0;
#                            padding: 20px;
#                        }
#
#
#                        .container {
#                            max-width: 800px;
#                            margin: 0 auto;
#                        }
#
#                        .post {
#                            background-color: #fff;
#                            padding: 20px;
#                            margin-bottom: 20px;
#                            border-radius: 12px;
#                            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
#                        }
#
#                        .post h1 {
#                            margin: 0 0 10px;
#                            font-size: 24px;
#                            color: #333;
#                        }
#
#                        .post p {
#                            color: #555;
#                            line-height: 1.6;
#                        }
#                    </style>
#                </head>
#                <body>
#
#                 <form method="post">
#                 <input type="text" name="title" id=""> <br><br>
#                 <input type="text" name="content" id=""> <br> <br>
#                 <button>submit</button>
#                 </form>
#
#
#                <div class="container">
#            """
#
#     for p in posts:
#         body += f"""
#                <div class="post">
#                    <h1>{p[1]}</h1>
#                    <p>{p[2]}</p>
#                </div>
#                """
#
#     body += """
#            </div>
#            </body>
#            </html>
#            """
#     return response(body)



from db.connect import DBManager
from units.http import response


def post_list():
    with DBManager() as cur:
        cur.execute("""SELECT * FROM postings""")
        posts = cur.fetchall()

    body = """
    <!DOCTYPE html>
    <html lang="uz">
    <head>
        <meta charset="UTF-8">
        <title>Posts</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea, #764ba2);
                margin: 0;
                padding: 0;
            }

            .container {
                max-width: 800px;
                margin: 50px auto;
            }

            .form-box {
                background: white;
                padding: 20px;
                border-radius: 12px;
                margin-bottom: 30px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }

            input {
                width: 100%;
                padding: 10px;
                margin-bottom: 10px;
                border-radius: 8px;
                border: 1px solid #ccc;
                font-size: 16px;
            }

            button {
                background: #764ba2;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 20px;
                cursor: pointer;
                transition: 0.3s;
            }

            button:hover {
                background: #5a3580;
            }

            .post {
                background: white;
                padding: 20px;
                margin-bottom: 20px;
                border-radius: 12px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }

            .post h1 {
                margin: 0 0 10px;
                font-size: 22px;
                color: #333;
            }

            .post p {
                color: #555;
                line-height: 1.6;
            }

            h2 {
                color: white;
                text-align: center;
            }
        </style>
    </head>
    <body>

        <div class="container">

            <h2>📝 Post yaratish</h2>

            <div class="form-box">
                <form method="post">
                    <input type="text" name="title" placeholder="Sarlavha..." required> <br>
                    <input type="text" name="content" placeholder="Matn..." required><br> 
                    <button type="submit">Yuborish</button>
                </form>
                
            </div>
            

    """

    # for p in posts:
    #     body += f"""
    #     <div class="post">
    #         <h1>{p[1]}</h1>
    #         <p>{p[2]}</p>
    #
    #     </div>
    #     """
    for p in posts:
        body += f"""
        <div class="post">
            <h1>{p[1]}</h1>
            <p>{p[2]}</p>

            <a href="/delete?id={{id}}">
    <button>Delete</button>
</a>

            <a href="/update?id={p[0]}">
                <button>Update</button>
            </a>

        </div>
        """
    body += """
        </div>
    </body>
    </html>
    """

    return response(body)