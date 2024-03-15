import json

DICT_DATA = 'data/quiz_data.json'

quiz_data = [
    {
        'question': 'Что такое Python?',
        'options': ['Язык программирования', 'Тип данных', 'Музыкальный инструмент', 'Змея на английском'],
        'correct_option': 0
    },
    {
        'question': 'Какой тип данных используется для хранения целых чисел?',
        'options': ['int', 'float', 'str', 'natural'],
        'correct_option': 0
    },
    {
        'question': 'Какой тип данных используется для хранения дробных чисел?',
        'options': ['int', 'float', 'str', 'natural'],
        'correct_option': 1
    },
    {
        'question': 'Какой тип данных используется для хранения строк?',
        'options': ['int', 'float', 'str', 'natural'],
        'correct_option': 2
    },
    {
        'question': 'Что хранит в себе переменная?',
        'options': ['Имя', 'Тип', 'Значение', 'Длину имени'],
        'correct_option': 2
    },
    {
        'question': 'Какая из следующих функция переобразует десячичное число в двоичное?',
        'options': ['hex', 'bin', 'oct', 'int'],
        'correct_option': 1
    },
    {
        'question': 'Какая из следующих функция возвращает длину строки?',
        'options': ['count', 'add', 'bool', 'len'],
        'correct_option': 3
    },
    {
        'question': 'Какой модуль в Python ипользуется для управения асинхронными функциями?',
        'options': ['asyncio', 'logging', 'aiogram', 'aiosqlite'],
        'correct_option': 0
    },
    {
        'question': 'Как создать пустой список в Python?',
        'options': ['0', '()', '[]', '{}'],
        'correct_option': 2
    },
    {
        'question': 'Что делает встроенная функция input()?',
        'options': ['Считывает целое число с клавиатуры', 'Считывает строку с клавиатуры', 'Считывает дробное число с клавиатуры', 'Считывает boolean значение с клавиатуры'],
        'correct_option': 1
    },
    # Добавьте другие вопросы
]

with open(DICT_DATA, 'w') as files:
    json.dump(quiz_data, files)
