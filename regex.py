import re

reg_name=re.compile(r'^[A-Za-zА-Яа-яЁё]+$')
reg_surname=re.compile(r'^[A-Za-zА-Яа-яЁё]+$')
reg_phone=re.compile(r'^[+]\d{1,3}\((\d{2})\)\d{7}$')
reg_email=re.compile(r'^[A-Za-z0-9]+@yandex\.ru$')


