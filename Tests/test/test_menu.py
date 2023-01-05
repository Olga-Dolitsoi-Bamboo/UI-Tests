import pytest
from Tests.Pages.LoginPage import Login
from Tests.Pages.MenuPage import Menu

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
        assert True

