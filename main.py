from datetime import datetime, time, timedelta
from models import Rates


rates = Rates()


def time_plus(time, timedelta):
    ''' function to add hours to time'''
    start = datetime(
        2000, 1, 1,
        hour=time.hour, minute=time.minute, second=time.second)
    end = start + timedelta
    return end.time()


def calculate_employee_payments(f):
    try:
        lines = f.readlines()  # each line is an employee's work week
        result_txt = open('result.txt', 'w')
        for line in lines:
            line_data = line.split(',')
            counter = 0
            pay_per_hour = []
            try:
                for data in line_data:  # each data in line data is an employee's work day
                    if counter == 0:
                        name = data.split('=')[0]
                        data = data.split('=')[1]
                    counter += 1
                    day = data[:2]
                    if day not in rates.week_days and day not in rates.weekend_days:
                        raise ValueError(
                            'Error: Day should be in MA/TU/WE/TH/FR/SA/SU format')
                    start_hour = time(int(data[2:7].replace(':', '')[:2]))
                    end_hour = time(int(data[8:13].replace(':', '')[:2]))
                    if end_hour < start_hour:
                        raise ValueError(
                            'Error : End hour must be greater than start hour')
                    time_delta = timedelta(hours=1)
                    while start_hour < end_hour:
                        # we calculate hour by hour rate and append it to a list. Later will sum all rates of hours worked
                        pay_per_hour.append(
                            rates.calculate_rate(day, start_hour.hour))
                        start_hour = time_plus(start_hour, time_delta)

                result_txt.write(name + ' has to charge: ' +
                                 str(sum(pay_per_hour)) + 'USD \n')
            except Exception as e:
                print('error here')
                result_txt.write(str(e)+'\n')
                continue
        result_txt = open('result.txt', 'r')
        return result_txt
    except Exception as e:
        print('Error!')
        result_txt.write(str(e))
        result_txt = open('result.txt', 'r')
        return result_txt


with open('data.txt', 'r') as f:
    print(calculate_employee_payments(f).readlines())


f.close()
