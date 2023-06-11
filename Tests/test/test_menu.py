import allure
import pytest
from Tests.Pages.LoginPage import Login
from Tests.Pages.MenuPage import Menu
from Tests.Constants import Data as dt


class TestClassMenu:

    @pytest.mark.parametrize("main_option,sub_option,verify_url", dt.CASE_1)
    def test_expand_option_and_go_to_page(self, my_app, main_option, sub_option, verify_url):
        with allure.step("Pages initialisation"):
            login_page = Login(my_app)
            menu_page = Menu(my_app)

        with allure.step("Login to the portal"):
            login_page.login_to_portal(dt.EMAIL_USERNAME, dt.EMAIL_PASSWORD)
        with allure.step("Expand orders menu"):
            menu_page.expand_options(main_option)
        with allure.step("Go to some page"):
            menu_page.scroll_to_sub_option(sub_option[0])
            menu_page.go_to_option(sub_option)
        with allure.step("Verify if is on page"):
            assert menu_page.is_on_some_page(verify_url)



