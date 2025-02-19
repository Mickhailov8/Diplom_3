from pages.main_page import MainPage
from pages.recovery_password_page import RecoveryPasswordPage
from pages.personal_account_page import PersonalAccountPage
from data import UserData
import allure

class TestRecoveryPassPage:

    @allure.title('Проверка успешного перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    @allure.description("Проверка успешного перехода с главной страницы в личный кабинет и далее на страницу "
                        "восстановления пароля, кликом по кнопке 'Восстановить пароль'")
    def test_success_recovery_pass(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_recovery_button()
        recovery_page = RecoveryPasswordPage(driver)
        assert recovery_page.check_recovery_page_title()

    @allure.title("Проверка перехода на экран 'Восстановление пароля' после ввода пароля и клика по кнопке "
                  "'Восстановить'")
    @allure.description("Проверка ввода почты и клика по кнопке 'Восстановить'")
    def test_input_email_and_click_button_success(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_recovery_button()
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.set_email(UserData.USER_EMAIL)
        recovery_page.click_button_recovery()
        assert recovery_page.check_recovery_pass_title()

    @allure.title("Проверка работы кнопки раскрытия пароля 'Глазик' на экране восстановления пароля")
    @allure.description("На экране смены пароля кликаем на 'Глазик' для отображения скрытого пароля и проверяем"
                        " что поле становится активным")
    def test_eye_button_show_password_success(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_recovery_button()
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.set_email(UserData.USER_EMAIL)
        recovery_page.click_button_recovery()               # Нажать кнопку "Восстановить"
        recovery_page.set_new_password(UserData.NEW_PASSWORD)
        old_state = recovery_page.get_password_input_state()
        recovery_page.click_show_password_button()
        new_state = recovery_page.get_password_input_state()
        assert (old_state is False and new_state is True)
