from units.http import response

import os


def not_found():
    # Hozirgi fayl joylashgan papkani topish
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_path = os.path.join(base_dir, "templates", "404_not_found.html")

    with open(template_path, 'r', encoding='utf-8') as f:
        body = f.read()
    return response(body)



