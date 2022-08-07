from flask import Flask, request, current_app
from flask_cors import CORS
from typer import Typer 
from src.db.db import Selection, Panel, Authentication
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from datetime import datetime, timedelta
import jwt


runner = Typer()

Sel = Selection()
Pan = Panel()
Auth = Authentication()


app = Flask(__name__)
CORS(app, resources={
    r"/selection": {"origins": "*"},
    r"/upload_avater": {"origins": "*"},
    r"/check_panel" : {"origins": "*"},
    r"/panel/get_users" : {"origins": "*"},
    r"/panel/get_user_data" : {"origins": "*"},
    r"/login" : {"origins": "*"},
    }) # настройка CORS POLICY
app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'


@app.route('/selection', methods=['POST'])  # роут сборки шаблонов
def form1():
    passwd = Sel.new_user(request.json["data"])
    return {
        "status": "success", 
        "data" : {
            "password": passwd
            }
        }


@app.route('/panel/get_users', methods=['POST'])  # роут сборки шаблонов
def get_users():
    return {"status": "success", "data": Pan.all_users()}


@app.route('/panel/get_user_data', methods=['POST'])  # роут сборки шаблонов
def get_user_data():
    return {"status": "success", "data": Pan.one_user(request.json["user_id"])}


@app.route('/login', methods=('POST',))
def login():
    data = request.get_json()
    user_email = Auth.check_auth(**data)

    if not user_email:
        return { 'message': 'Проверьте данные', 'authenticated': False }, 401

    token = jwt.encode({
        'sub': user_email,
        'iat':datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        current_app.config['SECRET_KEY'])
    return { 'token': token.decode('UTF-8'), 'authenticated': False }


# @app.route('/check_email', methods=['POST'])  # роут сборки шаблонов
# def check_email():
#     return {"data": DBG.user_data(request.json["data"]["email"])}


# @app.route('/upload_avatea', methods=['POST'])  # роут сборки шаблонов
# def upload_avatar():
#     f = request.files['file']
#     f.save(secure_filename(f.filename))
#     return 'file uploaded successfully'


# @app.route('/login', methods=['POST'])  # роут сборки шаблонов
# def check_panel():
#     if request.json["passwrd"] == "fnJjggYix97z1syu" and request.json["email"] == "admin@admin.com":
#         token = jwt.encode({
#         'sub': request.json["email"],
#         'iat':datetime.utcnow(),
#         'exp': datetime.utcnow() + timedelta(minutes=30)},
#         current_app.config['SECRET_KEY'])
#         return { "status" : True, "is_admin" : True, 'token': token.decode('UTF-8') }
#     return {"status" : False, "is_admin" : False}


@runner.command()
def runner():
    try:
        app.run(host="45.91.8.150", port="5600") # запуск сервераp
    except:
        app.run(host="localhost", port="5600") # запуск сервераp
    