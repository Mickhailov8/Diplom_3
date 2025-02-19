from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop
from pages.base_page import BasePage
from urls import Urls
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):
    @allure.step("Открыть в браузере страницу 'Stellar Burger'")
    def open(self):
        self.open_page(Urls.BASE_URL)

    @allure.step("Кликнуть по кнопке 'Лента заказов' в шапке страницы")
    def click_list_order_button(self):
        list_order_button = self.wait_and_find_element(MainPageLocators.LIST_ORDER_BTN)
        self.click_element(list_order_button)


    @allure.step("Кликнуть по 'Ингредиенту' в 'Конструкторе'")
    def click_ingredient_button(self):
        ingredients_list = self.wait_and_find_element(MainPageLocators.INGREDIENT_LIST)
        ingredients = ingredients_list.find_elements(*MainPageLocators.INGREDIENT_ITEM)
        second_ingredient = ingredients[1]
        self.click_element(second_ingredient)

    @allure.step("Кликнуть по кнопке закрытия всплывающего окна")
    def close_ingredient_card(self):
        x_button = self.wait_and_find_element(MainPageLocators.X_BUTTON)
        self.click_element(x_button)

    @allure.step("Перетащить булку в зону создания бургера")
    def add_bun_in_order(self):
        source = self.wait_and_find_element(MainPageLocators.BUN_INGREDIENT)
        target = self.wait_and_find_element(MainPageLocators.BURGER_ORDER)
        drag_and_drop(self.driver, source, target)

    @allure.step("Перетащить соус в зону создания бургера")
    def add_sauce_in_order(self):
        source = self.wait_and_find_element(MainPageLocators.SAUCE_INGREDIENT)
        target = self.wait_and_find_element(MainPageLocators.BURGER_ORDER)
        drag_and_drop(self.driver, source, target)

    @allure.step("Перетащить мясо в зону создания бургера")
    def add_meat_in_order(self):
        source = self.wait_and_find_element(MainPageLocators.MEAT_INGREDIENT)
        target = self.wait_and_find_element(MainPageLocators.BURGER_ORDER)
        drag_and_drop(self.driver, source, target)

    @allure.step("Кликнуть по кнопке 'Оформить заказ'")
    def click_create_order_button(self):
        account_button = self.wait_and_find_element(MainPageLocators.CREATE_ORDER_BTN)
        self.click_element(account_button)

    @allure.step("Получить количество ингредиентов из счётчика")
    def get_count_ingredient(self):
        counter_element = self.wait_and_find_element(MainPageLocators.COUNTER)
        return counter_element.text

    @allure.step("Получить Email для авторизации из сгенерированных данных")
    def get_user_email(self, user_response):
        email = user_response["email"]
        return email

    @allure.step("Получить Password для авторизации из сгенерированных данных")
    def get_user_password(self, user_response):
        password = user_response["password"]
        return password

    @allure.step("Кликнуть по кнопке 'Личный кабинет' в шапке страницы")
    def click_account_button(self):
        account_button = self.wait_and_find_element(MainPageLocators.BUTTON_ACCOUNT)
        self.click_element(account_button)


    @allure.step("Кликнуть по кнопке закрытия всплывающего окна")
    def click_order_card_x_button(self):
        x_button = self.wait_and_find_element(MainPageLocators.CLOSE_WINDOW_BTN)
        self.click_element(x_button)


    @allure.step("Получить номер оформленного заказа")
    def get_new_order_number(self):
        WebDriverWait(self.driver, 10).until(lambda driver: self.wait_and_find_element(MainPageLocators.NUMBER_NEW_ORDER).text != '9999')
        new_order_number_element = self.wait_and_find_element(MainPageLocators.NUMBER_NEW_ORDER)
        new_order_number = new_order_number_element.text
        return int(new_order_number)

    @allure.step("Проверить что открылась карточка с информацией об ингредиенте")
    def check_ingredient_title(self):
        if self.is_element_present(MainPageLocators.INGREDIENT_TITLE) == True:
            return True

    @allure.step("Проверить что карточка с информацией об ингредиенте закрылась")
    def check_main_page_title(self):
        if self.is_element_present(MainPageLocators.TITLE_MAIN_PAGE) == True:
            return True

    @allure.step("Дождаться пока откроется Главная страница")
    def find_main_page_title(self):
        return self.wait_and_find_element(MainPageLocators.TITLE_MAIN_PAGE)

    @allure.step("Дождаться пока откроется окно с деталями заказа")
    def find_create_order_description(self):
        return self.wait_and_find_element(MainPageLocators.CREATE_ORDER_DESCRIPTION)


    @allure.step("Сравнить URL текущей страницы с адресом страницы 'Лента заказов'")
    def check_order_list_url(self):
        return self.driver.current_url == (Urls.BASE_URL + Urls.LIST_ORDER_PAGE)