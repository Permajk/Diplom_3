from selenium.webdriver.common.by import By



class LoginLocators:
    # Емейл
    EMAIL = By.XPATH, "//label[text()='Email']/following-sibling::input"
    # Пароль
    PASSWORD = By.XPATH, "//input[@name='Пароль']"
    # Кнопка Войти
    BUTTON_LOGIN = By.XPATH, "//button[text()='Войти']"
