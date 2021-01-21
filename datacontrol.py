from bs4 import BeautifulSoup
import requests
import logging
import os
from sys import platform
import datetime
from daily import Daily

logger = logging
cwd = os.getcwd()
if platform == "win32":
    logger.basicConfig(
        filename=cwd+'\logs\datapy.log',
        level=logging.DEBUG,filemode='w',
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
elif platform == "linux" or platform == "linux2":
    logger.basicConfig(
        filename=cwd+'/logs/datapy.log',
        level=logging.DEBUG,filemode='w',
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
        
#------Allows us to log to console--------#
formatter = logging.Formatter("%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s", "%Y-%m-%d %H:%M:%S")
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(formatter)
# add the handler to the root logger
logger.getLogger().addHandler(console)
#-----------------------------------------#


def get_covid_data():
    url= "https://www.worldometers.info/coronavirus/country/lebanon/"

    logger.info(f"Getting Covid data from {url}")
    try:
        logger.info("Trying to get Url response")
        resp = requests.get(url)    
        resp.raise_for_status()
    except Exception as e:
        logger.error(f"{e}")
        raise Exception("Failed to get response from url")

    soup = BeautifulSoup(resp.text,"html.parser")
    try:
        logger.info("Getting number of cases, deaths and recoveries")
        cases = soup.select(".content-inner > div:nth-child(6) > div:nth-child(2) > span:nth-child(1)")[0].text#Replace to deal with comma seperated string numbers cases = int(soup.select(".content-inner > div:nth-child(6) > div:nth-child(2) > span:nth-child(1)")[0].text.replace(',',''))
        deaths = soup.select(".content-inner > div:nth-child(7) > div:nth-child(2) > span:nth-child(1)")[0].text
        recoveries = soup.select(".content-inner > div:nth-child(8) > div:nth-child(2) > span:nth-child(1)")[0].text
        today = datetime.datetime.now()
        #TODO NEEDS VALIDATION HERE
        daily = Daily(cases, deaths, recoveries, today)
        logger.debug(f"{daily}")
        logger.info("Cases: {}   Deaths: {}    Recoveries: {}".format(cases,deaths,recoveries))
    except Exception as e:
        logger.error("CSS selector changed, failed to get numbers")
        logger.error(e)
    return daily

