import pytest
from Tests.Pages.LoginPage import Login
from Tests.Pages.MenuPage import Menu
from Tests.Constants import SearchText as st
from Tests.Constants import Data as dt

USR_OLGA_LTD_CREDENTIAL_USERNAME= 'olga@bamboo-card.com'
USR_OLGA_LTD_CREDENTIAL_PASSWORD= 'Odol2706####'


class TestClassMenu:

    @pytest.mark.parametrize("main_option,sub_option,verify_url",
                             [
                                 (st.ORDERS_TEXT[0], st.ORDER_HISTORY_TEXT, st.ORDER_HISTORY_URL),
                                 (st.ORDERS_TEXT[0], st.SOPPING_CARTS_TEXT, st.SOPPING_CARTS_URL),
                                 (st.ORDERS_TEXT[0], st.CARDS_HISTORY_TEXT, st.CARDS_HISTORY_URL),
                                 (st.PRODUCTS_TEXT[0], st.PRODUCT_LIST_TEXT, st.PRODUCT_LIST_URL),
                                 (st.PRODUCTS_TEXT[0], st.CATALOGS_TEXT, st.CATALOGS_URL),
                                 (st.PRODUCTS_TEXT[0], st.PRODUCT_RULES_TEXT, st.PRODUCT_RULES_URL),
                                 (st.PRODUCTS_TEXT[0], st.INVENTORY_TEXT, st.INVENTORY_URL),
                                 (st.FINANCE_TEXT[0], st.INVOICES_TEXT, st.INVOICES_URL),
                                 (st.FINANCE_TEXT[0], st.FUNDING_TEXT, st.FUNDING_URL),
                                 (st.FINANCE_TEXT[0], st.RECONCILIATION_TEXT, st.RECONCILIATION_URL),
                                 (st.FINANCE_TEXT[0], st.TRANSACTIONS_TEXT, st.TRANSACTIONS_URL),
                                 (st.MARKETPLACES_TEXT[0], st.ENEBA_TEXT, st.ENEBA_URL),
                                 (st.MARKETPLACES_TEXT[0], st.GAMIVO_TEXT, st.GAMIVO_URL),
                                 (st.REPORTS_TEXT[0], st.BRANDS_REPORT_TEXT, st.BRANDS_REPORT_URL),
                             ])
    def test_expand_option_and_go_to_page(self, my_app, main_option, sub_option, verify_url):
        # Pages initialisation
        login_page = Login(my_app)
        menu_page = Menu(my_app)
        # Login to the portal
        login_page.login_to_portal(USR_OLGA_LTD_CREDENTIAL_USERNAME, USR_OLGA_LTD_CREDENTIAL_PASSWORD)
        # Expand orders menu
        menu_page.expand_options(main_option)
        # Go to Order History
        menu_page.scroll_to_sub_option(sub_option[0])
        menu_page.go_to_option(sub_option)
        assert menu_page.is_on_some_page(verify_url)
        # Tear down



