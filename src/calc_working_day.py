import datetime

class WorkingDayCalculator:
    def __init__(self, holidays):
        self.holidays = [h.date() for h in holidays]

    def is_weekend_or_holiday(self, date):
        """ Check if it's a weekend (Saturday or Sunday) or a holiday """
        return date.weekday() >= 5 or date.date() in self.holidays

    def get_previous_working_day(self, start_date):
        """ Finds the most recent previous working day (skipping weekends and holidays). """
        while self.is_weekend_or_holiday(start_date):
            start_date -= datetime.timedelta(days=1)
        return start_date

    def calculate_working_days(self):
        """ Calculates the last three valid working days (today, yesterday, and the day before yesterday), skipping weekends and holidays. """
        today = datetime.datetime.now()

        # Get today
        valid_today = self.get_previous_working_day(today)

        # Get yesterday
        valid_yesterday = self.get_previous_working_day(valid_today - datetime.timedelta(days=1))

        # Get the day before yesterday
        valid_erryesterday = self.get_previous_working_day(valid_yesterday - datetime.timedelta(days=1))

        # Return results
        return valid_today, valid_yesterday, valid_erryesterday


# List of holidays
holiday_list = [
    datetime.datetime(2024, 8, 15),
    datetime.datetime(2024, 10, 2),
    datetime.datetime(2024, 11, 1),
    datetime.datetime(2024, 11, 15),
    datetime.datetime(2024, 12, 25)
]

# Instantiate the WorkingDayCalculator class
calculator = WorkingDayCalculator(holiday_list)

# Calculate the working days
today, yesterday, erryesterday = calculator.calculate_working_days()

# Print results
print("Valid Today:", today.strftime('%Y-%m-%d'))
print("Valid Yesterday:", yesterday.strftime('%Y-%m-%d'))
print("Valid Erryesterday:", erryesterday.strftime('%Y-%m-%d'))
