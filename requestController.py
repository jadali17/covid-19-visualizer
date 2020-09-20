import requests



class RequestController:
    def __init__(self, requesturl):
        self.requestUrl = requesturl

    def get_data(self):
        page = requests.get(self.requestUrl)
        data = page.content
        return data

