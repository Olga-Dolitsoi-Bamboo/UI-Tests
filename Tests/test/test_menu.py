import pytest
from Tests.Pages.LoginPage import Login
from Tests.Pages.MenuPage import Menu
from Tests.Constants import SearchText as st
from Tests.Constants import Data as dt

USR_OLGA_LTD_CREDENTIAL_USERNAME= 'olga@bamboo-card.com'
USR_OLGA_LTD_CREDENTIAL_PASSWORD= 'Odol2706####'


@pytest.mark.usefixtures("app")
class TestClass:

    def test_expand_orders(self):
        # Pages initialisation
        login_page = Login(self.driver)
        menu_page = Menu(self.driver)
        # Login to the portal
        login_page.login_to_portal(USR_OLGA_LTD_CREDENTIAL_USERNAME, USR_OLGA_LTD_CREDENTIAL_PASSWORD)
        # Expand orders menu
        menu_page.expand_options(st.ORDERS_TEXT)
        # Go to Order History
        menu_page.go_to_option(st.ORDER_HISTORY_TEXT)
        assert menu_page.is_on_some_page(st.ORDER_HISTORY_URL)

