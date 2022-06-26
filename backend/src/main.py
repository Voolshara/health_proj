from flask import Flask, request
from flask_cors import CORS
from typer import Typer 


runner = Typer()


app = Flask(__name__)
CORS(app, resources={
    r"/article_data*": {"origins": "*"},
    }) # настройка CORS POLICY
app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'


@runner.command()
def runner():
    app.run(host="localhost", port="4600") # запуск сервераp