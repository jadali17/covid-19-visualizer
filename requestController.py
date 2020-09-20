import requests


class RequestHandler:
    def __init__(self, requestUrl):
        self.requestUrl = requestUrl

    def getData(self):
        data = requests.get("https://opendata.ecdc.europa.eu/covid19/casedistribution/xml/")
        return data
