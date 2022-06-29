from flask import Flask, request
from flask_cors import CORS
from typer import Typer 
from .db import DB_new


runner = Typer()
DBN = DB_new()

app = Flask(__name__)
CORS(app, resources={
    r"/new_user": {"origins": "*"},
    }) # настройка CORS POLICY
app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'


@app.route('/new_user', methods=['POST'])  # роут сборки шаблонов
def form1():
    DBN.create_new_user(request.json["data"])
    return {"status": "success"}
    

@runner.command()
def runner():
    app.run(host="localhost", port="4600") # запуск сервераp