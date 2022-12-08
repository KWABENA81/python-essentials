# This is a sample Python script.
import re


def run_code(emails=None):
    regx = r'[\w.+-]+@[\w-]+\.[\w.-]+'
    valid_emails = re.findall(regx, emails)
    for email in valid_emails:
        print(email)


def email_list():
    return 'abc@as.c2w  abc@as.com abc@as.009  abc@as. .c abc@as.c  abc@as.9c'


if __name__ == '__main__':
    run_code(email_list())


#               OUTPUT
# /usr/bin/python3.10 /home/sask/Documents/edureka/python-essentials/oop/Q4.py
# abc@as.c2w
# abc@as.com
# abc@as.009
# abc@as.c
# abc@as.9c
#
# Process finished with exit code 0