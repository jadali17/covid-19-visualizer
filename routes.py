from flask import Flask,render_template
from datacontrol import get_covid_data 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datacontrol import logger
from sqlalchemy import create_engine

#-----------------INITIALIZATION-------------------#
app = Flask(__name__)
app.config.from_object('config.DevConfig')
db = SQLAlchemy(app)
db_engine = create_engine("postgresql://postgres:postgres@localhost:5432/covid"	)

import models #needs to be imported after initializing db


#-------QUERIES----------------#
results = db_engine.execute("SELECT total_cases,total_deaths,total_recoveries FROM daily ORDER BY ID DESC LIMIT 1")
previousCases, previousDeaths, previousRecoveries = results.first()





#---------ROUTING---------------#
@app.route('/')
def index():
    data = get_covid_data()
    return "Cases: {}   Deaths: {}    Recoveries: {}".format(data.totalCases, data.totalDeaths, data.totalRecoveries)

@app.route('/home')
def home():
	data = get_covid_data()
	return render_template('main.html',cases = data.totalCases, deaths = data.totalDeaths, recoveries = data.totalRecoveries, today = data.date)

@app.route('/add')
def dataAdd():
    currentData = get_covid_data()
    newDaily = models.Daily(currentData)
    logger.info("Pushing totalCases:{} totalDeaths:{} totalRecoveries:{} to database".format(newDaily.total_cases, newDaily.total_deaths, newDaily.total_recoveries))
    newDaily.calculate(previousCases, previousDeaths, previousRecoveries)
    try:
        db.session.add(newDaily)
        db.session.commit()
    except Exception as e:
        logger.error("Key already exists")
        logger.error(e)
    
    return "Success in adding {}".format(newDaily)


#---------MAIN------------#
if __name__ == "__main__":
    app.run(debug=True)