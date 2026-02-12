import allure
from locators.main_locators import Mainlocators
from pages.base_page import BasePage



class MainPage(BasePage):
    
    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_for_element_hide(Mainlocators.OVERLAY)

    @allure.step('Клик по кнопке "Конструктор"')
    def click_button_constructor(self):
        self.click_on_element(Mainlocators.BUTTON_CONSTRUCTOR)

    @allure.step('Клик по кнопке «Лента заказов»')
    def click_button_feed_order(self):
        self.click_on_element(Mainlocators.BUTTON_FEED_ORDER)

    @allure.step('Клик по ингредиенту')
    def click_ingredient(self):
        self.click_on_element(Mainlocators.BUTTON_BUN)

    @allure.step('Открытие карточки ингредиента')
    def check_ingredient_info(self):
        return self.wait_for_element_is_displayed(Mainlocators.TEXT_BUN_INFO)

    @allure.step('Клик по крестику')
    def click_closed_button_bun_info(self):
        self.click_on_element(Mainlocators.BUTTON_BUN_INFO_CLOSED)

    @allure.step('Проверить закрытие карточки ингредиента')
    def check_closed_bun_info(self):
        return self.wait_for_element_is_displayed(Mainlocators.TEXT_PACK_BURGER)

    @allure.step('Ожидание кликабельности булочки')
    def wait_bun(self):
        self.wait_clickable_element(Mainlocators.BUTTON_BUN)

    @allure.step('Перетаскивание ингредиента в конструктор')
    def drag_and_drop_ingredients_to_burger_constructor(self):
        source_element = self.find_element_with_wait(Mainlocators.BUTTON_BUN)
        target_element = self.find_element_with_wait(Mainlocators.BURGER_CONSTRUCTOR)
        self.drag_and_drop_element(source_element, target_element)

    @allure.step('Получить количество ингредиентов')
    def get_count_ingredients(self):
        self.wait_for_element_is_displayed(Mainlocators.COUNT_BUN)
        return self.get_text_on_element(Mainlocators.COUNT_BUN)

    @allure.step('Переход по клику на "Конструктор" из "Ленты заказов"')
    def check_go_to_constructor(self):
        self.main_page_loading_wait()
        self.click_button_feed_order()
        self.main_page_loading_wait()
        self.click_button_constructor()
        self.main_page_loading_wait()

    @allure.step('Переход по клику на раздел "Лента заказов"')
    def check_go_to_feed_order(self):
        self.main_page_loading_wait()
        self.click_button_feed_order()
        self.main_page_loading_wait()

    @allure.step('Клик на ингредиент булочки открывает всплывающее окно с деталями')
    def click_ingredient_go_bun_info(self):
        self.main_page_loading_wait()
        self.click_ingredient()
        self.main_page_loading_wait()
        
    @allure.step('Всплывающее окно закрывается кликом по крестику')
    def click_ingredient_go_bun_info(self):
        self.main_page_loading_wait()
        self.click_ingredient()
        self.main_page_loading_wait()
        self.click_closed_button_bun_info()
        self.main_page_loading_wait()

    @allure.step('Добавлении ингредиента в заказ увеличивает счётчик этого ингредиента')
    def check_ingredient_counter_increases(self):
        self.main_page_loading_wait()
        self.wait_bun()
        self.drag_and_drop_ingredients_to_burger_constructor()
        self.main_page_loading_wait()

