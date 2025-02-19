from selenium.webdriver.common.by import By

class RecoveryPassPageLocators:


    RECOVER_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")          # Заголовок 'Восстановление пароля'
    FIELD_EMAIL = (By.XPATH, "//input[@class='text input__textfield text_type_main-default']")
    BUTTON_RECOVERY = (By.XPATH, "//button[text() = 'Восстановить']")
    RECOVER_PASS_TITLE = (By.XPATH, "//h2[text()= 'Восстановление пароля']")
    FIELD_NEW_PASSWORD = (By.XPATH, "//input[@name='Введите новый пароль']")

    EYE_BUTTON = (By. XPATH, "//div[contains(@class,'input__icon input__icon-action')]")
    PASSWORD_FIELD = (By.XPATH, "//input[@class='text input__textfield text_type_main-default'")
    BUTTON_ACCOUNT = (By.XPATH, "(.//a[@class = 'AppHeader_header__link__3D_hX'])[2]")
