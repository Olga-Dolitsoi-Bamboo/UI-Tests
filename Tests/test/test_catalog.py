from Pages.Catalogs.CatalogsPage import Catalogs
from Pages.LoginPage import Login
from Pages.MenuPage import Menu
from Constants import Data as dt
from Constants import SearchText as st


class TestClassCatalog:
    def test_crate_catalog(self, my_app):
        login_page = Login(my_app)
        menu_page = Menu(my_app)
        catalog_page = Catalogs(my_app)

        login_page.login_to_portal(dt.EMAIL_USERNAME, dt.EMAIL_PASSWORD)
        # Go to Brand page
        menu_page.expand_options(st.PRODUCTS_TEXT)
        menu_page.go_to_option(st.CATALOGS_TEXT)
        add_catalog = catalog_page.click_create_catalog()
        add_catalog.create_catalog(dt.CATALOG_NAME_CASE_1, dt.CATALOG_DISCOUNT_CASE_1, dt.CATALOG_DESCRIPTION_CASE_1,
                                   dt.CATALOG_SUPPLIER_FEE_CASE_1, dt.CATALOG_TRANSACTION_FEE_CASE_1)
        assert catalog_page.verify_catalog_exist(dt.CATALOG_NAME_CASE_1)

    # def test_user_can_add_client_to_catalog(self, my_app):
    #     login_page = Login(my_app)
    #     menu_page = Menu(my_app)
    #     catalog_page = Catalogs(my_app)
    #
    #     login_page.login_to_portal(dt.EMAIL_USERNAME, dt.EMAIL_PASSWORD)
    #     # Go to Brand page
    #     menu_page.expand_options(st.PRODUCTS_TEXT)
    #     menu_page.go_to_option(st.CATALOGS_TEXT)
    #     catalog_details = catalog_page.go_to_catalog(dt.CATALOG_IN_DB)
    #     catalog_details.go_to_clients_tab()
    #     add_client_popup = catalog_details.add_client_to_catalog()
    #     add_client_popup.add_client(dt.CATALOGS_CLIENT_TO_ADD)
    #     catalog_details.check_is_present_css(dt.CATALOGS_CLIENT_TO_ADD)



