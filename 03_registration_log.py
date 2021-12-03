# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

# TODO здесь ваш код

class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def analysis(line):
    global name, email, age
    print(f'Read line {line}', flush=True)
    name, email, age = line.split(' ')
    age = int(age)
    if not name or not email or age is None:
        print('Одно из зачений пустое, пока')
    if name.isalpha is True:
        print('В имени только буквы')
    if email.find('@') > -1 and email.find('.') > -1:
        print('Поле e-mail содержит и @ и точку')
    if 10 <= age <= 99:
        print('Возраст корректен')


def exceptions():
    if not name or not email or age is None:
        print('Одно из зачений пустое, пока')
        raise ValueError
    if name.isalpha is False:
        print('В имени помимо букв еще что-то')
        raise NotNameError
    if email.find('@') == -1 and email.find('.') == -1:
        print('Поле e-mail НЕ содержит @ или точку')
        raise NotEmailError
    if 10 < age or age > 99:
        print('Возраст не корректен')
        raise ValueError




with open('registrations.txt', 'r', encoding='utf8') as ff:
    for line in ff:
        line = line[:-1]
        try:
            analysis(line)
            exceptions()
        except ValueError as exc:
            pass
        except NotNameError as exc:
            pass
        except NotEmailError as exc:
            pass
