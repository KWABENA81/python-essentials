# This is a sample Python script.
import re


def run_code():
    dt = '''
       2012-10-12
       2032-09-12
       2012-13-12 
       2012-11-32 
       1972-01-12
       '''

    valid_dates = re.findall(r'(\d{4}\-(0[1-9]|1[0-2])\-(0[1-9]|[12][0-9]|3[01]))', dt)
    for valid_date in valid_dates:
        print(valid_date)


if __name__ == '__main__':
    run_code()



#       SOLUTION OUTPUT
# /usr/bin/python3.10 /home/sask/Documents/edureka/python-essentials/oop/Q7.py
# ('2012-10-12', '10', '12')
# ('2032-09-12', '09', '12')
# ('1972-01-12', '01', '12')