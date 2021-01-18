from bs4 import BeautifulSoup
import requests
import logging
import os
from sys import platform
from datetime import date

cwd = os.getcwd()
if platform == "win32":
    logging.basicConfig(
        filename=cwd+'\logs\datapy.log',
        level=logging.INFO,filemode='w',
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
elif platform == "linux" or platform == "linux2":
    logging.basicConfig(
        filename=cwd+'/logs/datapy.log',
        level=logging.INFO,filemode='w',
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
        
#------Allows us to log to console--------#
formatter = logging.Formatter("%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s", "%Y-%m-%d %H:%M:%S")
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger().addHandler(console)
#-----------------------------------------#


def get_covid_data():
    url= "https://www.worldometers.info/coronavirus/country/lebanon/"

    logging.info(f"Getting Covid data from {url}")
    try:
        logging.info("Trying to get Url response")
        resp = requests.get(url)    
        resp.raise_for_status()
    except Exception as e:
        logging.error(f"{e}")
        raise Exception("Failed to get response from url")

    soup = BeautifulSoup(resp.text,"html.parser")
    try:
        logging.info("Getting number of cases, deaths and recoveries")
        cases = int(soup.select(".content-inner > div:nth-child(6) > div:nth-child(2) > span:nth-child(1)")[0].text.replace(',','')) #Replace to deal with comma seperated string numbers
        deaths = int(soup.select(".content-inner > div:nth-child(7) > div:nth-child(2) > span:nth-child(1)")[0].text.replace(',',''))
        recoveries = int(soup.select(".content-inner > div:nth-child(8) > div:nth-child(2) > span:nth-child(1)")[0].text.replace(',',''))
        today = date.today()
        logging.info("Cases: {}   Deaths: {}    Recoveries: {}".format(cases,deaths,recoveries))
    except Exception as e:
        logging.error("CSS selector changed, failed to get numbers")
        logging.error(e)
    return cases, deaths, recoveries, today

