from requestController import RequestController
import pandas as pd

if __name__ == '__main__':
    url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/json/"
    requestHandler = RequestController(url)
    data = requestHandler.get_data()
    covidData = pd.read_json(data)
    print(covidData)
    #TODO Set up visualization on a webpage