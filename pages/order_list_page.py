from pages.base_page import BasePage
from locators.order_list_page_locators import OrderListPageLocators
import allure
from urls import Urls


class OrderListPage(BasePage):

    @allure.step("Открыть окно с деталями заказа кликом по карточке заказа")
    def click_order_card(self):
        order_card = self.wait_and_find_element(OrderListPageLocators.ORDER_CARD)
        self.click_element(order_card)


    @allure.step("Получить номер последнего заказа")
    def get_order_number(self):
        element = self.wait_and_find_element(OrderListPageLocators.ORDER_NUMBER_IN_HISTORY)
        return element.text

    @allure.step("Получить значение счётчика заказаов на странице 'Лента заказов'")
    def get_orders_counter(self):
        number = self.wait_and_find_element(OrderListPageLocators.ORDER_COUNTER)
        return int(number.text)

    @allure.step("Кликнуть по кнопке 'Конструктор' в шапке страницы")
    def click_constructor_button(self):
        constructor_button = self.wait_and_find_element(OrderListPageLocators.CONSTRUCTOR_BTN)
        self.click_element(constructor_button)

    @allure.step("Получить значение счётчика 'Выполнено за сегодня' заказаов на странице 'Лента заказов'")
    def get_orders_counter_today(self):
        number = self.wait_and_find_element(OrderListPageLocators.ORDER_COUNTER_TODAY)
        return int(number.text)

    @allure.step("Получить номер заказа в разделе 'В работе' на экране Ллента заказов'")
    def get_order_in_works_number(self):
        number_in_works = self.wait_and_find_element(OrderListPageLocators.ORDER_IN_WORK)
        return int(number_in_works.text)

    @allure.step("Проверить что открылось окно с деталями заказа")
    def check_open_window_with_order_details(self):
        return self.is_element_present(OrderListPageLocators.INGREDIENT_IN_ORDER)

    @allure.step("Сравнить URL текущей страницы с адресом главной страницы")
    def check_main_page_url(self):
        return self.driver.current_url == Urls.BASE_URL
