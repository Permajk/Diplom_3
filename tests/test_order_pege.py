import allure
from pages.order_page import OrderPage



class TestOrderPage:

    @allure.title('Проверка, что при создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_check_rise_counter_order_to_all_time(self, login):
        # Авторизация
        driver = login
        order = OrderPage(driver)
        # Заходим в ленту заказов
        order.check_go_to_feed_order()
        # Получаем количество заказов "Выполнено за всё время" до оформления нового заказа
        order_all_time_before = order.text_order_all_time()
        # Оформляем новый заказ
        order.check_maiking_a_new_order()
        # Заходим в ленту заказов и получаем количество заказов "Выполнено за всё время" после оформления заказа
        order.click_button_feed_order()
        order_all_time_after = order.text_order_all_time()
        # Проверяем, что общее количество заказов увеличилось на один
        assert int(order_all_time_before) + 1 == int(order_all_time_after)


    @allure.title('Проверка, что при создании нового заказа счётчик "Выполнено за сегодя" увеличивается')
    def test_check_rise_counter_order_to_today(self, login):
        # Авторизация
        driver = login
        order = OrderPage(driver)
        # Заходим в ленту заказов
        order.check_go_to_feed_order()
        # Получаем количество заказов "Выполнено за сегодня" до оформления нового заказа
        order_today_before = order.text_order_today()
        # Оформляем новый заказ
        order.check_maiking_a_new_order()
        # Заходим в ленту заказов и получаем количество заказов "Выполнено за сегодня" после оформления заказа
        order.click_button_feed_order()
        order_today_after = order.text_order_today()
        # Проверяем, что общее количество заказов увеличилось на один
        assert int(order_today_before) + 1 == int(order_today_after)


    @allure.title('Проверка, что после оформления заказа его номер появляется в разделе "В работе"')
    def test_check_number_order_in_work(self, login):
        # Авторизация
        driver = login
        order = OrderPage(driver)
        # Переход в карточку заказа
        order.check_number_in_order_card()
        # Получение номера заказа из карточки заказа
        order_number = order.text_order_number()
        # Закрытие карточки заказа
        order.click_button_order_exit()
        # Переход в "Ленту заказов"
        order.click_button_feed_order()
        # Получение номера заказа в разделе "В работе"
        order_number_in_work = order.text_order_number_in_work()
        # Проверяем, что номер заказа появился в разделе "В работе"
        assert order_number in order_number_in_work
        