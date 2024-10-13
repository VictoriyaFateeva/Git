import re

reg_name=re.compile(r'^[A-Za-zА-Яа-яЁё]+$')
reg_surname=re.compile(r'^[A-Za-zА-Яа-яЁё]+$')
reg_phone=re.compile(r'^[+]\d{1,3}\((\d{2})\)\d{7}$')
reg_email=re.compile(r'^[A-Za-z0-9]+@yandex\.ru$')


user_name=input('Введите имя пользователя:')
if bool(reg_name.match(user_name)) is True:
    print('Имя принято!')
else:
    print('Ввод некорректен! Повторите ввод данных!\n')

user_surname=input('Введите фамилию пользователя:')
if bool(reg_surname.match(user_surname)) is True:
    print('Фамилия принята!')
else:
    print('Ввод некорректен! Повторите ввод данных!\n')

user_phone=input('Введите номер пользователя:')
if bool(reg_phone.match(user_phone)) is True:
    print('Номер принят!')
else:
    print('Ввод некорректен! Повторите ввод данных!\n')

user_email=input('Введите почту пользователя:')
if bool(reg_email.match(user_email)) is True:
    print('Почта принята!')
else:
    print('Ввод некорректен! Повторите ввод данных!\n')

print('Хочу пушить в прод')