import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


def test_version_1_1():
    url = "https://passport.yandex.ru/auth/"

    # Добавьте Ваш логин и пароль
    login = ''
    password = ''

    driver = webdriver.Chrome()
    driver.get(url)

    # Если надо выбрать аккаунт для входа, выбираем Войти в другой аккаунт
    try:
        xpath = '// *[ @ id = "root"] / div / div[2] / div[2] / div / div / div[2] / div[3] / div / div / div / div / a / span[2]'
        another_accaunt_button = driver.find_element("xpath", xpath)
        another_accaunt_button.click()
    except NoSuchElementException:
        print("Нет входа через аккаунт")
    else:
        print("Вход через аккаунт")
        time.sleep(2)

    # нажмем кнопку "почта", так как иногда бывает выбрано "телефон"
    try:
        xpath = '// *[ @ id = "root"] / div / div[2] / div[2] / div / div / div[2] / div[3] / div / div / div / div[1] / form / div[1] / div[1] / button'
        email_login_button = driver.find_element("xpath", xpath)
        email_login_button.click()
    except NoSuchElementException:
        print("Кнопка Почта не найдена")
    else:
        print("Находим и нажимаем кнопку Почта")

    # Вводим логин и нажимаем кнопку Войти
    xpath = '//*[@id="passp-field-login"]'
    email_form = driver.find_element("xpath", xpath)
    email_form.clear()
    email_form.send_keys(login)
    button_inter = driver.find_element("xpath", '// *[ @ id = "passp:sign-in"]')
    button_inter.click()
    time.sleep(1)

    # Вводим пароль и нажимаем кнопку
    password_form = driver.find_element("xpath", '// *[ @ id = "passp-field-passwd"]')
    password_form.clear()
    password_form.send_keys(password)

    button_password = driver.find_element("xpath", '// *[ @ id = "passp:sign-in"]')# time.sleep(1)
    button_password.click()
    time.sleep(5)

    # ищем элементы, которые должны быть на главной странице
    xpaths = {}
    xpaths['left_id'] = '// *[ @ id = "__next"] / div / header / div[1]'
    xpaths['main menu Главная'] = '// *[ @ id = "__next"] / div / header / div[2] / div / nav / ul / li[1] / a'
    xpaths['data_xpath'] = '//*[@id="__next"]/div/main/div/div[2]/div[1]/h2/a'
    xpaths['data_xpath2'] = '// *[ @ id = "__next"] / div / main / div / div[2] / div[1] / h2 / a'
    xpaths['Поиск настроек2'] = '// *[ @ id = "__next"] / div / header / div[3] / div[1] / div / div'
    xpaths['мои контакты'] = '// *[ @ id = "__next"] / div / main / div / div[2] / div[2] / div / a[4]'
    xpaths['меню Безопасность'] = '// *[ @ id = "__next"] / div / header / div[2] / div / nav / ul / li[6] / a'

    print()

    for key, xpath in xpaths.items():
        try:
            element = driver.find_element("xpath", xpath)
        except NoSuchElementException:
            print(f"{key} element Не найден")
            assert False
        else:
            print(f'{key} element.text:', element.text)
            assert True
    time.sleep(1)

if __name__ == '__main__':
    pytest.main(['tests/test_selen.py'])
