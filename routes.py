from flask import Flask
from datacontrol import get_covid_data 
app = Flask(__name__)


@app.route('/')
def index():
    cases, deaths, recoveries, today = get_covid_data()
    return f"{str(cases)}  {str(deaths)}  {str(recoveries)}  {str(today)}"
if __name__ == "__main__":
    app.run(debug=True)