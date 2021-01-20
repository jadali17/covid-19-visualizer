from routes import db

class Daily(db.Model):
    __tablename__ = 'daily'

    date = db.Column(db.String(), primary_key=True)
    total_cases = db.Column(db.String())
    total_deaths = db.Column(db.String())
    total_recoveries = db.Column(db.String())

    def __init__(self, totalCases, totalRecoveries, totalDeaths, today):
        self.totalCases = totalCases
        self.totalRecoveries = totalRecoveries
        self.totalDeaths = totalDeaths
        self.date = today

    def __repr__(self):
        return '<id {}>'.format(self.date)