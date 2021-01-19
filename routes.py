from flask import Flask,render_template
from datacontrol import get_covid_data 



app = Flask(__name__)


@app.route('/')
def index():
    daily = get_covid_data()

    return "Cases: {}   Deaths: {}    Recoveries: {}".format(daily.totalCases, daily.totalDeaths, daily.totalRecoveries)

@app.route('/home')
def home():
	daily = get_covid_data()
	return render_template('main.html',cases = daily.totalCases, deaths = daily.totalDeaths, recoveries = daily.totalRecoveries, today = daily.date)

if __name__ == "__main__":
    app.run(debug=True)