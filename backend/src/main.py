from flask import Flask, request, current_app
from flask_cors import CORS
from typer import Typer 
from src.db.db import DB_new, DB_get, DB_panel
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import jwt
from datetime import datetime, timedelta


runner = Typer()
DBN = DB_new()
DBPANEL = DB_panel()

app = Flask(__name__)
CORS(app, resources={
    r"/form_selection": {"origins": "*"},
    r"/upload_avater": {"origins": "*"},
    r"/check_panel" : {"origins": "*"},
    r"/panel/get_users" : {"origins": "*"},
    r"/panel/get_user_data" : {"origins": "*"},
    }) # настройка CORS POLICY
app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'


@app.route('/form_selection', methods=['POST'])  # роут сборки шаблонов
def form1():
    DBN.create_new_user(request.json["data"])
    return {"status": "success"}

@app.route('/upload_avatea', methods=['POST'])  # роут сборки шаблонов
def upload_avatar():
    f = request.files['file']
    f.save(secure_filename(f.filename))
    return 'file uploaded successfully'

@app.route('/login', methods=['POST'])  # роут сборки шаблонов
def check_panel():
    if request.json["passwrd"] == "fnJjggYix97z1syu" and request.json["email"] == "admin@admin.com":
        token = jwt.encode({
        'sub': request.json["email"],
        'iat':datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        current_app.config['SECRET_KEY'])
        return { "status" : True, "is_admin" : True, 'token': token.decode('UTF-8') }
    return {"status" : False, "is_admin" : False}


@app.route('/panel/get_users', methods=['POST'])  # роут сборки шаблонов
def get_users():
    return {"data": DBPANEL.get_all_users()}


@app.route('/panel/get_user_data', methods=['POST'])  # роут сборки шаблонов
def get_user_data():
    return {"data": DBPANEL.get_user_data(request.json["user_id"])}

@runner.command()
def runner():
    # app.run(host="localhost", port="5600") # запуск сервераp
    app.run(host="45.91.8.150", port="5600") # запуск сервераp