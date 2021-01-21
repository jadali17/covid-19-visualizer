from routes import db

class Daily(db.Model):
	__tablename__ = 'daily'

	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.DateTime())
	total_cases = db.Column(db.Integer())
	total_deaths = db.Column(db.Integer())
	total_recoveries = db.Column(db.Integer())
	daily_cases = db.Column(db.Integer())
	daily_deaths = db.Column(db.Integer())
	daily_recoveries = db.Column(db.Integer())
	def __init__(self, currentDay):
		self.total_cases = int(currentDay.totalCases.replace(',',''))
		self.total_recoveries = int(currentDay.totalRecoveries.replace(',',''))
		self.total_deaths = int(currentDay.totalDeaths.replace(',','')) 
		self.date = currentDay.date

	def __repr__(self):
		return '<id {}>'.format(self.id)
		
	def calculate(self, cases, deaths, recoveries ):
		self.daily_cases = self.total_cases-cases
		self.daily_deaths = self.total_deaths-deaths
		self.daily_recoveries = self.total_recoveries-recoveries
