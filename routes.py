from flask import Flask,render_template
from datacontrol import get_covid_data 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from loggerModule import logger
from sqlalchemy import create_engine
from apscheduler.schedulers.background import BackgroundScheduler


#-----------------INITIALIZATION-------------------#
app = Flask(__name__)
app.config.from_object('config.DevConfig')
db = SQLAlchemy(app)
db_engine = create_engine("postgresql://postgres:postgres@localhost:5432/covid"	)

import models #needs to be imported after initializing db


#-------QUERIES----------------#
results = db_engine.execute("SELECT total_cases,total_deaths,total_recoveries, date FROM daily ORDER BY ID DESC LIMIT 1")
previousCases, previousDeaths, previousRecoveries, date  = results.first()


#---------HELPER FUNCTIONS-------------#
def dataAdd(db):
    currentData = get_covid_data()
    newDaily = models.Daily(currentData)
    logger.info("Pushing totalCases:{} totalDeaths:{} totalRecoveries:{} to database".format(newDaily.total_cases, newDaily.total_deaths, newDaily.total_recoveries))
    newDaily.calculate(previousCases, previousDeaths, previousRecoveries)
    time = newDaily.date
    try:
        db.session.add(newDaily)
        db.session.commit()
    except Exception as e:
        logger.error("Key already exists")
        logger.error(e)
    logger.info("Successfuly added to database")

#----------------TASK SCHEDULER---------------#
scheduler = BackgroundScheduler(daemon = True)
scheduler.add_job(dataAdd,'interval',args=[db],days=1)
scheduler.start()


#---------ROUTING---------------#
@app.route('/')
def index():
    data = get_covid_data()
    return "Cases: {}   Deaths: {}    Recoveries: {}".format(data.totalCases, data.totalDeaths, data.totalRecoveries)

@app.route('/home')
def home():
    currentData = get_covid_data()
    logger.debug(currentData.totalDeaths)
    logger.debug(previousDeaths)
    newDaily = models.Daily(currentData)
    newDaily.calculate(previousCases, previousDeaths, previousRecoveries)
    return render_template('main.html',cases = currentData.totalCases, deaths = currentData.totalDeaths, recoveries = currentData.totalRecoveries, today = date, dailyCases = newDaily.daily_cases, dailyDeaths= newDaily.daily_deaths, dailyRecoveries = newDaily.daily_recoveries )

@app.route('/add')
def dataAdd():
    currentData = get_covid_data()
    newDaily = models.Daily(currentData)
    logger.info("Pushing totalCases:{} totalDeaths:{} totalRecoveries:{} to database".format(newDaily.total_cases, newDaily.total_deaths, newDaily.total_recoveries))
    newDaily.calculate(previousCases, previousDeaths, previousRecoveries)
    time = newDaily.date
    logger.info(time)
    try:
        db.session.add(newDaily)
        db.session.commit()
    except Exception as e:
        logger.error("Key already exists")
        logger.error(e)
    logger.info("Successfuly added to database")
    return "Success in adding {}".format(newDaily)


#---------MAIN------------#
if __name__ == "__main__":
    app.run(host="192.168.2.123",debug=True)