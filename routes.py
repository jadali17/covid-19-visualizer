from flask import Flask,render_template
from datacontrol import get_covid_data 
app = Flask(__name__)


@app.route('/')
def index():
    cases, deaths, recoveries, today = get_covid_data()

    return "Cases: {}   Deaths: {}    Recoveries: {}".format(cases,deaths,recoveries)

@app.route('/home')
def home():
	cases, deaths, recoveries, today = get_covid_data()
	return render_template('main.html',cases = cases, deaths = deaths, recoveries = recoveries, today = today)

if __name__ == "__main__":
    app.run(debug=True)