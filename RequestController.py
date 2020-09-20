import pandas as pd
import requests


class RequestController:
    def __init__(self, url):
        self.url = url

    def read_json(self):
        df = pd.read_json(self.get_data())
        return df

    def get_data(self):
        request = requests.get(self.url)
        data = request.content
        return data


# @visualize_app.route('/')
# def hello_world():
#     return "Hello"

