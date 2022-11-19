import pytest

from homework4 import (

# Задание 1 Найди страну
find_country_1, find_country_2,

# Задание 2 Уникальные значения
getorigin,

# Задание 3 Процент слов
getdefinotion,

# Задание 4 yandex
scryopt_for, scryopt_max,

# Задание 5(Необязательное)
dict_from_list1, dict_from_list2, dict_list, dict_list2,
dict_list22, dict_list_rec
)

funcs_for_tests = [dict_from_list1, dict_from_list2, dict_list, dict_list2,
dict_list22, dict_list_rec]

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

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

list_1 = ['2018-01-01', 'yandex', 'cpc', 100, '2018-01-02', 'yandex', 'cpc', 200, '2018-01-01', 'rambler', 'cpc', 300]

@pytest.mark.parametrize("func", [find_country_1, find_country_2])
def test_country(func):
    result = func(geo_logs)
    for item in result:
        assert 'Россия' in list(item.values())[0]
    for item in result:
        assert 'Россия' == list(item.values())[0][1]

def test_getorigin():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    resultids = {98, 35, 15, 213, 54, 119}
    result = getorigin(ids)
    assert result == resultids
    assert isinstance(result, set)
    for item in result:
        assert any(item in v for v in ids.values())

def test_scryopt_max():
    yandex = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    assert 'yandex' == scryopt_max(yandex)
    google = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 121, 'email': 42, 'ok': 98}
    assert 'google' == scryopt_max(google)

@pytest.mark.parametrize("func", funcs_for_tests[2:])
def test_funcs_dict_list_1(func):
    testlist = ['2018-01-01', 'yandex', 'cpc', 100]
    testresult = {'2018-01-01': {'yandex': {'cpc': 100}}}
    result = func(testlist)
    assert testresult == result

@pytest.mark.parametrize("func", funcs_for_tests[2:])
def test_funcs_dict_list_2(func):
    list_1 = ['2018-01-01', 'yandex', 'cpc', 100, '2018-01-02',
              'yandex', 'cpc', 200, '2018-01-01', 'rambler', 'cpc', 300]
    result = func(list_1)
    for i in list_1[:-1]:
        k = next(iter(result))
        assert i == k
        result = result.get(k)
    assert result == list_1[-1]


if __name__ == '__main__':
    pytest.main(['test_4_pytest.py'])