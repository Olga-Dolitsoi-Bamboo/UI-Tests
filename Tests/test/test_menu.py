import pytest
from Tests.Pages.LoginPage import Login
from Tests.Pages.MenuPage import Menu
from Tests.Constants import SearchText as st
from Tests.Constants import Data as dt


class TestClassMenu:

    @pytest.mark.parametrize("main_option,sub_option,verify_url", dt.CASE_1)
    def test_expand_option_and_go_to_page(self, my_app, main_option, sub_option, verify_url):
        # Pages initialisation
        login_page = Login(my_app)
        menu_page = Menu(my_app)
        # Login to the portal
        login_page.login_to_portal(dt.EMAIL_USERNAME, dt.EMAIL_PASSWORD)
        # Expand orders menu
        menu_page.expand_options(main_option)
        # Go to Order History
        menu_page.scroll_to_sub_option(sub_option[0])
        menu_page.go_to_option(sub_option)
        assert menu_page.is_on_some_page(verify_url)
        # Tear down



