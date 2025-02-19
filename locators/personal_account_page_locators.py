from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    FIELD_EMAIL = (By.XPATH, "//input[@class='text input__textfield text_type_main-default'][1]")
    FIELD_PASSWORD = (By.XPATH, "//input[@name='Пароль']")
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")
    DESCRIPTION_ACCOUNT = (By.XPATH, "//p[text() = 'В этом разделе вы можете изменить свои персональные данные']")
    ORDER_HISTORY_BTN = (By.XPATH, "//a[text()='История заказов']")
    EXIT_BTN = (By.XPATH, "//button[text()='Выход']")
    TITLE_LOGIN_PAGE = (By.XPATH, "//h2[text()='Вход']")
    TITLE_MAIN_PAGE = (By.XPATH, "//h1[text() = 'Соберите бургер']")
    ORDER_NUMBER_IN_HISTORY = (By.XPATH, "(//p[contains(@class, 'text text_type_digits-default')])[1]")
    RECOVERY_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")  # Кнопка 'Восстановить пароль'