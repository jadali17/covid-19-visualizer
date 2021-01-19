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