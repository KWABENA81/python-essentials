# This is a sample Python script.
import re


def run_check():
    ssn_cda = '''
       201-210-123
       201 672 788
       4894 409 33
       938022999
       '''

    valids = re.findall(r'(\d{3}(\-|\s)\d{3}(\-|\s)\d{3})', ssn_cda)
    for sn in valids:
        print(sn)


if __name__ == '__main__':
    run_check()



#       SOLUTION OUTPUT
# /usr/bin/python3.10 /home/sask/Documents/edureka/python-essentials/oop/Q2.py
# ('201-210-123', '-', '-')
# ('201 672 788', ' ', ' ')
