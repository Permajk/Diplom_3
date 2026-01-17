import allure
from locators.order_locators import OrderLocators
from pages.base_page import BasePage




class OrderPage(BasePage):

    @allure.step('Дождаться загрузки страницы')
    def order_page_loading_wait(self):
        self.wait_for_element_hide(OrderLocators.OVERLAY)

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_button_feed_order(self):
        self.click_on_element(OrderLocators.BUTTON_FEED_ORDER)

    @allure.step('Получить количество заказов за всё время')
    def text_order_all_time(self):
        return self.get_text_on_element(OrderLocators.TEXT_ORDER_ALL_TIME)

    @allure.step('Получить количество заказов за сегодня')
    def text_order_today(self):
        return self.get_text_on_element(OrderLocators.TEXT_ORDER_TODAY)

    @allure.step('Клик по кнопке «Конструктор»')
    def click_button_constructor(self):
        self.click_on_element(OrderLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Ожидание кликабельности булочки')
    def wait_bun(self):
        self.wait_clickable_element(OrderLocators.BUTTON_BUN)

    @allure.step('Перетаскивание ингредиента в конструктор бургера')
    def drag_and_drop_ingredients_to_burger_constructor(self):
        source_element = self.find_element_with_wait(OrderLocators.BUTTON_BUN)
        target_element = self.find_element_with_wait(OrderLocators.BURGER_CONSTRUCTOR)
        self.drag_and_drop_element(source_element, target_element)

    @allure.step('Оформить заказ')
    def click_create_order(self):
        self.click_on_element(OrderLocators.BUTTON_PLACE_ORDER)

    @allure.step('Ожидаем видимости текста в карточке заказа')
    def wait_until_text_order_visible(self):
        self.wait_for_element(OrderLocators.TEXT_ORDER_INFO)

    @allure.step('Убеждаемся, что номер заказа не 9999')
    def incorrect_number_invisible(self):
        self.wait_for_element_hide(OrderLocators.INCORRECT_NUMBER)

    @allure.step('Закрытия карточки с заказом')
    def click_button_order_exit(self):
        self.click_on_element(OrderLocators.BUTTON_ORDER_EXIT)
        self.order_page_loading_wait()

    @allure.step('Получить номер в карточке заказа после оформления')
    def text_order_number(self):
        self.wait_for_element(OrderLocators.ORDER_NUMBER)
        return self.get_text_on_element(OrderLocators.ORDER_NUMBER)

    @allure.step('Получить номер заказа в работе в Ленте заказов')
    def text_order_number_in_work(self):
        self.wait_for_element(OrderLocators.ORDER_NUMBER_IN_WORK)
        return self.get_text_on_element(OrderLocators.ORDER_NUMBER_IN_WORK)



    @allure.step('Переход в Ленту заказов')
    def check_go_to_feed_order(self):
        self.order_page_loading_wait()
        self.click_button_feed_order()
        self.order_page_loading_wait()

    @allure.step('Оформление нового заказа')
    def check_maiking_a_new_order(self):
        self.order_page_loading_wait()
        self.click_button_constructor()
        self.order_page_loading_wait()
        self.wait_bun()
        self.drag_and_drop_ingredients_to_burger_constructor()
        self.order_page_loading_wait()
        self.click_create_order()
        self.order_page_loading_wait()
        self.wait_until_text_order_visible()
        self.order_page_loading_wait()
        self.incorrect_number_invisible()
        self.order_page_loading_wait()
        self.click_button_order_exit()
        self.order_page_loading_wait()


    @allure.step('Переход в карточку заказа')
    def check_number_in_order_card(self):
        self.order_page_loading_wait()
        self.click_button_constructor()
        self.order_page_loading_wait()
        self.wait_bun()
        self.drag_and_drop_ingredients_to_burger_constructor()
        self.order_page_loading_wait()
        self.click_create_order()
        self.order_page_loading_wait()
        self.wait_until_text_order_visible()
        self.order_page_loading_wait()
        self.incorrect_number_invisible()
        self.order_page_loading_wait()
