from bs4 import BeautifulSoup
import requests
import logging
from loggerModule import logger
import os
from sys import platform
import datetime




#------Allows us to log to console--------#

formatter = logging.Formatter("%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s", "%Y-%m-%d %H:%M:%S")
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
# add the handler to the root logger
logger.getLogger().addHandler(console)

#--------CLASSES----------------#
class Daily:
	def __init__(self, totalCases, totalRecoveries, totalDeaths, today):
		self.totalCases = totalCases
		self.totalRecoveries = totalRecoveries
		self.totalDeaths = totalDeaths
		self.date = today
	def calculate(self, previousDay):
		self.dailyCases = self.totalCases - previousDay.totalCases 
		self.dailyRecoveries = self.totalRecoveries - previousDay.totalRecoveries
		self.dailyDeaths = self.totalDeaths - previousDay.totalDeaths

#----------Functions----------------#
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
        recoveries = soup.select(".content-inner > div:nth-child(7) > div:nth-child(2) > span:nth-child(1)")[0].text
        deaths = soup.select(".content-inner > div:nth-child(8) > div:nth-child(2) > span:nth-child(1)")[0].text
        today = datetime.datetime.now()
        #TODO NEEDS VALIDATION HERE
        daily = Daily(cases, deaths, recoveries, today)
        logger.debug(f"{daily}")
        logger.info("Cases: {}   Deaths: {}    Recoveries: {}".format(cases,deaths,recoveries))
    except Exception as e:
        logger.error("CSS selector changed, failed to get numbers")
        logger.error(e)
    return daily

