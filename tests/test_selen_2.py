import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


# Функция ожидания элементов
def wait_of_element_located(xpath, driver_init):
    element = WebDriverWait(driver_init, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element

# Вынесем инициализцию драйвера в отдельную фикстуру pytest
@pytest.fixture
def driver_init():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)  # , executable_path=r'C:/Users/…/…/chromedriver.exe')
    driver.get("https://passport.yandex.ru/auth/")
    yield driver
    driver.close()


def test_auth_user(driver_init):

    # # Добавьте Ваш логи и пароль
    login = ''
    password = ''

    # нажмем кнопку "почта", так как иногда бывает выбрано "телефон"
    xpath = '// *[ @ id = "root"] / div / div[2] / div[2] / div / div / div[2] / div[3] / div / div / div / div[1] / form / div[1] / div[1] / button'
    wait_of_element_located(xpath, driver_init).click()

    # Вводим логин и нажимаем кнопку Войти
    xpath = '//*[@id="passp-field-login"]'
    email_form = wait_of_element_located(xpath, driver_init)
    email_form.clear()
    email_form.send_keys(login)
    button_inter = driver_init.find_element("xpath", '// *[ @ id = "passp:sign-in"]')
    button_inter.click()

    # Вводим пароль и нажимаем кнопку
    xpath = '// *[ @ id = "passp-field-passwd"]'
    password_form = wait_of_element_located(xpath, driver_init)
    password_form.clear()
    password_form.send_keys(password)
    button_password = driver_init.find_element("xpath", '// *[ @ id = "passp:sign-in"]')# time.sleep(1)
    button_password.click()

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
    wait_of_element_located(xpaths['left_id'], driver_init)

    for key, xpath in xpaths.items():
        try:
            element = driver_init.find_element("xpath", xpath)
        except NoSuchElementException:
            print(f"{key} element Не найден")
            assert False
        else:
            print(f'{key} element.text:', element.text)
            assert True
    time.sleep(5)

if __name__ == '__main__':
    # pytest.main(['tests/test_selen_2.py'])
    test_auth_user(driver_init=driver_init)
