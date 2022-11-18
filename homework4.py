# Задание 1
'''
Дан список с визитами по городам и странам. Напишите код, который возвращает
отфильтрованный список geo_logs, содержащий только визиты из России.
'''
from pprint import pprint

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

def find_country_1(geo_logs: list, country='Россия'):
    ''' Фильтрует список по одной стране с помощью цикла '''
    geo_logs_filter = []
    for geo_log in geo_logs:
        if list(geo_log.values())[0][1] == country.capitalize():
            geo_logs_filter.append(geo_log)
    return geo_logs_filter

def find_country_2(geo_logs: list, country='Россия'):
    ''' Фильтрует список по одной стране с помощью функций filter и lambda '''
    return list(filter(lambda n: list(n.values())[0][1] == country.capitalize(), geo_logs))

# Задание 2
'''
Выведите на экран все уникальные гео-ID из значений словаря ids.
Т.е. список вида [213, 15, 54, 119, 98, 35]
'''

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def getorigin(ids):
       set_id = set()
       for list_id in ids.values():
              set_id.update(list_id)
       return set_id

# Задание 3
'''
Дан список поисковых запросов. Получить распределение количества слов в них. 
Т.е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.
'''

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'спорт',
    'спор',
    'новости',
    'ищу плавки с меховым капюшоном',
    'плыву по реке ищу способ не заржаветь больше чем есть'
    ]


def getdefinotion(queries):
    dict_queries = {}
    for query in queries:
        l_query = len(query.split())
        dict_queries.setdefault(l_query, [0, 0])
        dict_queries[l_query][0] += 1
        dict_queries[l_query][1] = round(dict_queries[l_query][0] / len(queries) * 100, 2)
    return dict_queries


# Задание 4
'''
Дана статистика рекламных каналов по объемам продаж.
Напишите скрипт, который возвращает название канала с максимальным объемом.
Т.е. в данном примере скрипт должен возвращать 'yandex'.
'''

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

def scryopt_max(stats):

    return max(stats.items(), key=lambda n: n[1])[0]

def scryopt_for(stats):

    max_ = ['', 0]
    for key, value in stats.items():
        if max_[1] < value:
            max_ = key, value
    return max_[0]


# Задание 5(Необязательное)
'''
Напишите код для преобразования произвольного списка вида
['2018-01-01', 'yandex', 'cpc', 100]
(он может быть любой длины) в словарь
{'2018-01-01': {'yandex': {'cpc': 100}}}
'''

from pprint import pprint

list_1 = ['2018-01-01', 'yandex', 'cpc', 100, '2018-01-02', 'yandex', 'cpc', 200, '2018-01-01', 'rambler', 'cpc', 300]

list_2 = [
    ['2018-01-01', 'yandex', 'cpc', 100],
    ['2018-01-02', 'yandex', 'cpc', 200],
    ['2018-01-01', 'rambler', 'cpc', 300],
    ['2018-01-01', 'rambler', 'cpm', 800],
    ['2018-01-02', 'yandex', 'cpm', 1000],
    ['2018-01-03', 'yandex', 'cpc', 400]
]


# Функции с жутким списком - мое первое понимание решения этой задачи
def dict_from_list1(list_):
    ''' Жутский список 1 '''
    dict_1 = {}
    for item in range(0, len(list_), 4):
        dict_1.setdefault(list_[item], {})
        dict_1[list_[item]].setdefault(list_[item + 1], {})
        dict_1[list_[item]][list_[item + 1]].setdefault(list_[item + 2], list_[item + 3])

    return dict_1


def dict_from_list2(list_):
    ''' Жутский список 2 '''
    dict_2 = {}
    for date, res, cpc, data in list_:
        dict_2.setdefault(date, {})
        dict_2[date].setdefault(res, {})
        dict_2[date][res].setdefault(cpc, data)
    return dict_2


def dict_list(list_):
    ''' Создает словарь словарей из списка прямым проходом '''
    dict_result = dict_int = {}
    for item in range(0, len(list_) - 2):
        dict_int.setdefault(list_[item], {})
        dict_int = dict_int[list_[item]]
    dict_int[list_[item + 1]] = list_[item + 2]
    return dict_result


def dict_list2(list_):
    ''' Создает словарь словарей с конца списка '''
    dict_ = {list_[-2]: list_[-1]}
    for item in range(len(list_) - 3, -1, -1):
        dict_ = {list_[item]: dict_}
    return dict_


def dict_list22(list_input):
    ''' Классическое решение '''
    list_ = list_input.copy()
    dict_ = list_.pop()
    for elem in range(len(list_)):
        dict_ = {list_.pop(): dict_}
    return dict_


def dict_list_rec(list_):
    ''' Неидеальная рекурсия '''
    list_i = list_.copy()
    if len(list_) == 2:
        return {list_i.pop(0): list_i.pop(0)}
    return {list_i.pop(0): dict_list_rec(list_i)}


def update_dict_lists(list_):
    dict_main = {}
    for item in list_:
        dict_item = dict_list(item)
        dict_main.update(dict_item)
    return dict_main