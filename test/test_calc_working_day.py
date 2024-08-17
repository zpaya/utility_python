import unittest
import datetime
from src.calc_working_day import WorkingDayCalculator  # Assuming the class is saved in this file

class TestWorkingDayCalculator(unittest.TestCase):

    def setUp(self):
        # Set up a fixed list of holidays for the tests
        self.holiday_list = [
            datetime.datetime(2024, 8, 15),
            datetime.datetime(2024, 10, 2),
            datetime.datetime(2024, 11, 1),
            datetime.datetime(2024, 11, 15),
            datetime.datetime(2024, 12, 25)
        ]
        self.calculator = WorkingDayCalculator(self.holiday_list)

    def test_is_weekend_or_holiday(self):
        # Test weekends
        saturday = datetime.datetime(2024, 8, 10)
        sunday = datetime.datetime(2024, 8, 11)
        self.assertTrue(self.calculator.is_weekend_or_holiday(saturday))
        self.assertTrue(self.calculator.is_weekend_or_holiday(sunday))

        # Test holidays
        holiday = datetime.datetime(2024, 8, 15)
        self.assertTrue(self.calculator.is_weekend_or_holiday(holiday))

        # Test a normal weekday (not a weekend or holiday)
        weekday = datetime.datetime(2024, 8, 14)
        self.assertFalse(self.calculator.is_weekend_or_holiday(weekday))

    def test_get_previous_working_day(self):
        # Test to get previous working day from a weekend
        monday = datetime.datetime(2024, 8, 12)  # Monday
        saturday = datetime.datetime(2024, 8, 10)
        previous_working_day = self.calculator.get_previous_working_day(saturday)
        self.assertEqual(previous_working_day.date(), monday.date() - datetime.timedelta(days=1))

        # Test to get previous working day from a holiday
        post_holiday = datetime.datetime(2024, 8, 16)
        previous_working_day = self.calculator.get_previous_working_day(post_holiday)
        self.assertEqual(previous_working_day.date(), datetime.datetime(2024, 8, 14).date())  # Aug 14 is the last working day before Aug 15

    def test_calculate_working_days(self):
        # Assuming today's date is fixed for the test
        fixed_today = datetime.datetime(2024, 8, 16)
        
        # Override the calculator's method to return fixed date for now()
        self.calculator.get_previous_working_day = lambda date: fixed_today

        today, yesterday, erryesterday = self.calculator.calculate_working_days()

        # Test today
        self.assertEqual(today.strftime('%Y-%m-%d'), '2024-08-16')

        # Test yesterday
        self.assertEqual(yesterday.strftime('%Y-%m-%d'), '2024-08-15')

        # Test the day before yesterday
        self.assertEqual(erryesterday.strftime('%Y-%m-%d'), '2024-08-14')

if __name__ == '__main__':
    unittest.main()
