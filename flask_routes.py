from flask import Flask
from RequestController import RequestController

flask_app = Flask(__name__)
request_controller = RequestController("https://opendata.ecdc.europa.eu/covid19/casedistribution/json/")
df = request_controller.read_json()


@flask_app.route('/')
def show_df():
    return print(df)
