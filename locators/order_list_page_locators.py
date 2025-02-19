from selenium.webdriver.common.by import By

class OrderListPageLocators:
    ORDER_CARD = (By.XPATH, "(//a[contains(@class,'OrderHistory_link__1iNby')])[2]")
    INGREDIENT_IN_ORDER = (By.XPATH, "(//div[contains(@class,'Modal_imgBox__27yrH')])[1]")
    ORDER_NUMBER_IN_HISTORY = (By.XPATH, "(//p[contains(@class, 'text text_type_digits-default')])[1]")
    ORDER_COUNTER = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number__2MbrQ')])[1]")
    ORDER_COUNTER_TODAY = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number__2MbrQ')])[2]")
    NUMBER_READY_ORDER = (By.XPATH, "(//li[contains(@class, 'text text_type_digits-default')])[2]")
    ORDER_IN_WORK = (By.XPATH, "(//li[contains(@class, 'text text_type_digits-default mb-2')])[6][1]")
    CONSTRUCTOR_BTN = (By.XPATH, "//p[text()='Конструктор']")