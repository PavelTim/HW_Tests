import homework4
import unittest

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
dict_list22, dict_list_rec, update_dict_lists
)


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

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

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

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

list_1 = ['2018-01-01', 'yandex', 'cpc', 100, '2018-01-02', 'yandex', 'cpc', 200, '2018-01-01', 'rambler', 'cpc', 300]

# print(dir(homework4))

class TestHW1(unittest.TestCase):

    def test_country_1(self):
        result = find_country_1(geo_logs)
        # print(result)
        for item in result:
            self.assertIn('Россия', list(item.values())[0])
        for item in result:
            self.assertEqual('Россия', list(item.values())[0][1])


    def test_country_2(self):
        result = find_country_2(geo_logs)
        for item in result:
            self.assertIn('Россия', list(item.values())[0])
        for item in result:
            self.assertEqual('Россия', list(item.values())[0][1])


    def test_getorigin(self):
        ids = {'user1': [213, 213, 213, 15, 213],
               'user2': [54, 54, 119, 119, 119],
               'user3': [213, 98, 98, 35]}
        resultids = {98, 35, 15, 213, 54, 119}
        result = getorigin(ids)
        self.assertSetEqual(result, resultids)
        self.assertTrue(isinstance(result, set))
        for item in result:
            self.assertTrue(any(item in v for v in ids.values()))


    def test_scryopt_max(self):
        yandex = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
        self.assertEqual('yandex', scryopt_max(yandex))
        google = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 121, 'email': 42, 'ok': 98}
        self.assertEqual('google', scryopt_max(google))


    # def test_dict_from_list1(self):
    #     testlist = ['2018-01-01', 'yandex', 'cpc', 100]
    #     testresult = {'2018-01-01': {'yandex': {'cpc': 100}}}
    #     result = dict_from_list1(testlist)
    #     self.assertDictEqual(testresult, result)
    #     result = dict_from_list1(list_1)
    #     for i in list_1:
    #         k = next(iter(result)) if isinstance(result, dict) else result
    #         self.assertEqual(i, k)
    #         result = result.get(k) if isinstance(result, dict) else result
    #
    # def test_dict_from_list2(self):
    #     testlist = ['2018-01-01', 'yandex', 'cpc', 100]
    #     testresult = {'2018-01-01': {'yandex': {'cpc': 100}}}
    #     result = dict_from_list2(testlist)
    #     self.assertDictEqual(testresult, result)
    #     result = dict_from_list2(list_1)
    #     for i in list_1:
    #         k = next(iter(result)) if isinstance(result, dict) else result
    #         self.assertEqual(i, k)
    #         result = result.get(k) if isinstance(result, dict) else result
    # ======================================
    def test_dict_list(self):
        testlist = ['2018-01-01', 'yandex', 'cpc', 100]
        testresult = {'2018-01-01': {'yandex': {'cpc': 100}}}
        result = dict_list(testlist)
        self.assertDictEqual(testresult, result)
        result = dict_list(list_1)
        for i in list_1:
            k = next(iter(result)) if isinstance(result, dict) else result
            self.assertEqual(i, k)
            result = result.get(k) if isinstance(result, dict) else result

    def test_dict_list2(self):
        testlist = ['2018-01-01', 'yandex', 'cpc', 100]
        testresult = {'2018-01-01': {'yandex': {'cpc': 100}}}
        result = dict_list2(testlist)
        self.assertDictEqual(testresult, result)
        result = dict_list2(list_1)
        for i in list_1:
            k = next(iter(result)) if isinstance(result, dict) else result
            self.assertEqual(i, k)
            result = result.get(k) if isinstance(result, dict) else result


    def test_dict_list22(self):
        testlist = ['2018-01-01', 'yandex', 'cpc', 100]
        testresult = {'2018-01-01': {'yandex': {'cpc': 100}}}
        result = dict_list22(testlist)
        self.assertDictEqual(testresult, result)
        result = dict_list22(list_1)
        for i in list_1:
            k = next(iter(result)) if isinstance(result, dict) else result
            self.assertEqual(i, k)
            result = result.get(k) if isinstance(result, dict) else result


    def test_dict_list_rec(self):
        testlist = ['2018-01-01', 'yandex', 'cpc', 100]
        testresult = {'2018-01-01': {'yandex': {'cpc': 100}}}
        result = dict_list_rec(testlist)
        self.assertDictEqual(testresult, result)
        result = dict_list_rec(list_1)
        for i in list_1:
            k = next(iter(result)) if isinstance(result, dict) else result
            self.assertEqual(i, k)
            result = result.get(k) if isinstance(result, dict) else result


if __name__ == '__main__':
    unittest.main()