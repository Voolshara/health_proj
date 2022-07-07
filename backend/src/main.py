from flask import Flask, request
from flask_cors import CORS
from typer import Typer 
from src.db.db import DB_new
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage


runner = Typer()
DBN = DB_new()

app = Flask(__name__)
CORS(app, resources={
    r"/new_user": {"origins": "*"},
     r"/upload_avater": {"origins": "*"},
    }) # настройка CORS POLICY
app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'


@app.route('/new_user', methods=['POST'])  # роут сборки шаблонов
def form1():
    DBN.create_new_user(request.json["data"])
    return {"status": "success"}

@app.route('/upload_avatea', methods=['POST'])  # роут сборки шаблонов
def upload_avatar():
    f = request.files['file']
    f.save(secure_filename(f.filename))
    return 'file uploaded successfully'
    

@runner.command()
def runner():
    app.run(host="localhost", port="5600") # запуск сервераp