import allure
from data import Urls
from pages.main_page import MainPage



class TestMainPage:

    allure.title('Проверка перехода по клику на "Конструктор" из "Ленты заказов"')
    def test_check_go_to_constructor(self, driver):
        main = MainPage(driver)
        main.check_go_to_constructor()
        assert main.get_current_url() == Urls.url_main


    @allure.title('Проверка перехода по клику на раздел "Лента заказов"')
    def test_check_go_to_feed_order(self, driver):
        main = MainPage(driver)
        main.check_go_to_feed_order()
        assert main.get_current_url() == Urls.url_order


    @allure.title('Проверка, что клик по ингредиенту(булочке) открывает всплывающее окно с деталями')
    def test_click_ingredient_go_bun_info(self, driver):
        main = MainPage(driver)
        main.click_ingredient_go_bun_info()
        assert main.check_ingredient_info() == True


    @allure.title('Проверка, что всплывающее окно закрывается кликом по крестику')
    def test_click_ingredient_go_bun_info(self, driver):
        main = MainPage(driver)
        main.click_ingredient_go_bun_info()
        assert main.check_closed_bun_info() == True


    @allure.title('Проверка, что добавление ингредиента в заказ увеличивает счётчик этого ингредиента')
    def test_check_ingredient_counter_increases(self, driver):
        main = MainPage(driver)
        main.check_ingredient_counter_increases()
        main.main_page_loading_wait()
        assert main.get_count_ingredients() == '2'
