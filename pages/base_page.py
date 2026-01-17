import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



class BasePage:
    
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Подождать видимости элемента')
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Клик по элементу на странице')
    def click_on_element(self, locator):
        target = self.wait_clickable_element(locator)
        click = ActionChains(self.driver)
        click.move_to_element(target).click().perform()

    @allure.step('Ввести текст в поле ввода')
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step('Получить текст элемента')
    def get_text_on_element(self, locator):
        element = self.wait_for_element(locator)
        return element.text


    @allure.step('Подождать пока элемент не станет невидимым')
    def wait_for_element_hide(self, locator):
        return WebDriverWait(self.driver, timeout=10).until(EC.invisibility_of_element_located(locator))

    @allure.step('Перетащить элемент в корзину')
    def drag_and_drop_element(self, source_element, target_element):
        ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()
    
    @allure.step('Найти элемент с ожиданием')
    def find_element_with_wait(self, locator, timeout=10):
        return self.wait_for_element(locator, timeout)

    @allure.step('Получить адрес страницы')
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Подождать и проверить отображение элемента на странице')
    def wait_for_element_is_displayed(self, locator, timeout=10):
        return self.wait_for_element(locator, timeout).is_displayed()
    
    @allure.step('Подождать кликабельности элемента')
    def wait_clickable_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    