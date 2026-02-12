from selenium.webdriver.common.by import By



class Mainlocators:
    # Загрузка страницы
    OVERLAY = By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"
    # Кнопка Конструктор
    BUTTON_CONSTRUCTOR = By.XPATH, "//p[text()='Конструктор']"
    # Кнопка Лента заказов
    BUTTON_FEED_ORDER = By.XPATH, "//p[text()='Лента Заказов']"
    # Текст Лента заказов
    TEXT_FEED_ORDER = By.XPATH, "//h1[text()='Лента Заказов']"
    # Кнопка Флюоресцентная булка
    BUTTON_BUN = By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']"
    # Текст Детали ингредиента в карточке Флюоресцентной булки
    TEXT_BUN_INFO = By.XPATH, "//h2[text()='Детали ингредиента']"
    # Кнопка крестик в карточке Флюоресцентной булки
    BUTTON_BUN_INFO_CLOSED = By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"
    # Текст Собери Бургер
    TEXT_PACK_BURGER = By.XPATH, "//h1[text()='Соберите бургер']" 
    # Область для перетаскивания ингредиентов
    BURGER_CONSTRUCTOR = By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]"
    # Счётчик у булочки
    COUNT_BUN = By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]//p[contains(@class, 'counter_counter__num')][1]"
