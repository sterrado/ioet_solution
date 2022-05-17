
class Rates():
    def __init__(self):
        self.week_days = ['MO', 'TU', 'WE', 'TH', 'FR']
        self.weekend_days = ['SA', 'SU']

    def calculate_rate(self, day, hour):
        if day in self.week_days:
            if 0 < hour <= 9:
                hour_rate = 25
            elif 9 < hour <= 18:
                hour_rate = 15
            elif hour == 00 or (18 < hour <= 23):
                hour_rate = 20
            return hour_rate
        elif day in self.weekend_days:
            if 0 < hour <= 9:
                hour_rate = 30
            elif 9 < hour <= 18:
                hour_rate = 20
            elif hour == 00 or (18 < hour <= 23):
                hour_rate = 25
            return hour_rate
