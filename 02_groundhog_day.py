# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
# https://goo.gl/JnsDqu
# TODO здесь ваш код

from random import randint

ENLIGHTENMENT_CARMA_LEVEL = 777
CARMA = 0


class IamGodError(Exception):
    def __init__(self):
        pass

    def log_to_file(self):
        write_str = 'Ошибка, я не бог' + '\n'
        with open('out_log.txt', 'r+', encoding='utf8') as writing:
            file_eof = int(len(writing.read()))
            writing.write(write_str)


class DrunkError(Exception):
    def log_to_file(self):
        write_str = 'Ошибка, я напился' + '\n'
        with open('out_log.txt', 'r+', encoding='utf8') as writing:
            file_eof = int(len(writing.read()))
            writing.write(write_str)


class CarCrashError(Exception):
    def log_to_file(self):
        write_str = 'Ошибка, я выпилился' + '\n'
        with open('out_log.txt', 'r+', encoding='utf8') as writing:
            file_eof = int(len(writing.read()))
            writing.write(write_str)


class GluttonyError(Exception):
    def log_to_file(self):
        write_str = 'Ошибка, я объелся' + '\n'
        with open('out_log.txt', 'r+', encoding='utf8') as writing:
            file_eof = int(len(writing.read()))
            writing.write(write_str)


class DepressionError(Exception):
    def log_to_file(self):
        write_str = 'Ошибка, я в депрессии' + '\n'
        with open('out_log.txt', 'r+', encoding='utf8') as writing:
            file_eof = int(len(writing.read()))
            writing.write(write_str)


class SuicideError(Exception):
    def log_to_file(self):
        write_str = 'Ошибка, убился' + '\n'
        with open('out_log.txt', 'r+', encoding='utf8') as writing:
            file_eof = int(len(writing.read()))
            writing.write(write_str)


def one_day():
    global CARMA
    dice_carma_level = randint(1, 7)
    CARMA += dice_carma_level
    dice_exception = randint(1, 78)
    carma_exception = dice_exception
    if carma_exception == 1:
        try:
            raise IamGodError()
        except IamGodError as exc:
            IamGodError.log_to_file(None)
            CARMA -= dice_carma_level
    if carma_exception == 14:
        try:
            raise DrunkError()
        except DrunkError as exc:
            DrunkError.log_to_file(None)
            CARMA -= dice_carma_level
    if carma_exception == 27:
        try:
            raise CarCrashError()
        except CarCrashError as exc:
            CarCrashError.log_to_file(None)
            CARMA -= dice_carma_level
    if carma_exception == 40:
        try:
            raise GluttonyError()
        except GluttonyError as exc:
            GluttonyError.log_to_file(None)
            CARMA -= dice_carma_level
    if carma_exception == 53:
        try:
            raise DepressionError()
        except DepressionError as exc:
            DepressionError.log_to_file(None)
            CARMA -= dice_carma_level
    if carma_exception == 66:
        try:
            raise SuicideError()
        except SuicideError as exc:
            SuicideError.log_to_file(None)
        CARMA -= dice_carma_level
    print(CARMA)


while CARMA != ENLIGHTENMENT_CARMA_LEVEL:
    if CARMA >= 777:
        CARMA = 777
    groundhog = one_day()
