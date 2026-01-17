from selenium.webdriver.common.by import By



class OrderLocators:
    # Загрузка страницы
    OVERLAY = By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"
    # Кнопка Лента заказов
    BUTTON_FEED_ORDER = By.XPATH, "//p[text()='Лента Заказов']"
    # Текст Выполнено за все время
    TEXT_ORDER_ALL_TIME = By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"
    # Текст Выполнено за сегодня
    TEXT_ORDER_TODAY = By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p"
    # Кнопка Конструктор
    BUTTON_CONSTRUCTOR = By.XPATH, "//p[text()='Конструктор']"
    # Кнопка Флюоресцентная булка
    BUTTON_BUN = By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']"
    # Область для перетаскивания ингредиентов
    BURGER_CONSTRUCTOR = By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]"
    # Кнопка Оформить заказ
    BUTTON_PLACE_ORDER = By.XPATH, "//button[text()='Оформить заказ']"
    # Текст Ваш заказ начали готовить в карточке заказа
    TEXT_ORDER_INFO = By.XPATH, "//p[text()='Ваш заказ начали готовить']"
    # Номер заказа 9999
    INCORRECT_NUMBER = By.XPATH, "//h2[contains(.,'9999')]"
    # Кнопка крестик в карточке заказа
    BUTTON_ORDER_EXIT = By.XPATH, "//div[contains(@class, 'Modal_modal__')]//button[contains(@class, 'close')]"
    # Номер заказа карточке заказа после оформления
    ORDER_NUMBER = By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow' )]"
    # Номер заказа в работе в Ленте заказов
    ORDER_NUMBER_IN_WORK = By.XPATH, "//li[contains(@class, 'text') and contains(@class, 'text_type_digits-default') and contains(@class, 'mb-2')]"


