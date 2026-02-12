import pytest
from selenium import webdriver
from data import Urls
from pages.login_page import LoginPage
from data import LoginData


# Фикстура для запуска тестов в двух браузерах
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Urls.url_main)
    yield driver
    driver.quit()

# Фикстура для авторизации пользователя
@pytest.fixture()
def login(driver):
    driver.get(Urls.url_login)
    login_page = LoginPage(driver)
    login_page.login(LoginData.email,LoginData.password)
    return driver
