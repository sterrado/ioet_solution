import unittest
import main


class TestMain(unittest.TestCase):

    def test_main_functions(self):
        data_file = open('data.txt', 'r')
        function_result = main.calculate_employee_payments(
            data_file).readlines()
        expected_result = open('result.txt', 'r').readlines()
        self.assertEquals(function_result, expected_result)

    def test_endhour_greater_than_starthour(self):
        expected_result = open('result_hour_error.txt', 'r').readlines()
        hour_error_data = open('data_hour_error.txt', 'r')
        self.assertEquals(expected_result, main.calculate_employee_payments(
            hour_error_data).readlines())

    def test_day_format(self):
        expected_result = open('result_day_error.txt', 'r').readlines()
        hour_error_data = open('data_day_error.txt', 'r')
        self.assertEquals(expected_result, main.calculate_employee_payments(
            hour_error_data).readlines())


if __name__ == '__main__':
    unittest.main()
