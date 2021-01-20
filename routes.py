from flask import Flask,render_template
from datacontrol import get_covid_data 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datacontrol import logger
app = Flask(__name__)
app.config.from_object('config.DevConfig')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import models # should be placed here for it to migrate

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
    data = get_covid_data()
    newDaily = models.Daily(totalCases = data.totalCases, totalDeaths = data.totalDeaths, totalRecoveries = data.totalRecoveries, today = str(data.date))
    logger.info("Pushing {} to database".format(newDaily))
    try:
        db.session.add(newDaily)
        db.session.commit()
    except Exception as e:
        logger.error("Key already exists")
        logger.error(e)
    
    return "Success in adding{}".format(data)

if __name__ == "__main__":
    app.run(debug=True)