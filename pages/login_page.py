import allure
from locators.login_locators import LoginLocators
from pages.base_page import BasePage



class LoginPage(BasePage):

    @allure.step('Авторизоваться')
    def login(self, email, password):
        self.send_keys_to_input(LoginLocators.EMAIL, email)
        self.send_keys_to_input(LoginLocators.PASSWORD, password)
        self.click_on_element(LoginLocators.BUTTON_LOGIN)
        