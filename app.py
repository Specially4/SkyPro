# ----------------------------
# PyCharm v.2021.3.3.
# Python v.3.9.10(64-\bit)
# Flask v.2.1.1
# ----------------------------

from flask import Flask
import json

with open('candidates.json', encoding='utf-8') as file:
    stock = json.load(file)


app = Flask(__name__)

@app.route("/")  # Главная страница, со списком кандидатов
def page_index():
    list_candidates = ''
    for i in stock:
        list_candidates += f'<pre>Имя - {i["name"]}<br>Позиция: {i["position"]}' \
                           f'<br>Навыки: {i["skills"]}</pre>'

    return (f'<h2>Главная страничка</h2>' + list_candidates)


@app.route("/candidates/<x>")  # Поиск кандидатов по ID
def page_candidates(x):
    for i in stock:
        if x in str(i['id']):
            return (f'<img src={i["picture"]}>' + f'<pre>Имя - {i["name"]}<br>Позиция: '
                                                  f'{i["position"]}<br>Навыки: {i["skills"]}</pre>')
            break
        else:
            continue

@app.route("/skills/<x>")  # Поиск кандидатов по скиллам
def page_skills(x):
    list_candidates = ''
    for i in stock:
        r = i["skills"].split(", ")
        if x.lower() in r:
            list_candidates += f'<pre>Имя - {i["name"]}<br>Позиция: {i["position"]}' \
                               f'<br>Навыки: {i["skills"]}</pre>'
    return list_candidates

app.run()
