import allure
import pytest

from Tests.Pages.LoginPage import Login
from Tests.Pages.MenuPage import Menu
from Tests.Constants import Data as dt
from Tests.Constants import SearchText as st
from Tests.Pages.Suppliers.SuppliersPage import Suppliers
from Tests.Pages.Suppliers.SupplierDetailPage import SupplierDetails


class TestSuppliers:

    @pytest.mark.parametrize('supplier, supp_acc', dt.SUPPLIER_CASE_1)
    def test_suppliers_accounts(self, my_app, supplier, supp_acc):
        with allure.step("Pages init"):
            login_page = Login(my_app)
            menu_page = Menu(my_app)
            suppliers_page = Suppliers(my_app)
            supplier_details = SupplierDetails(my_app)

        with allure.step("Login to portal"):
            login_page.login_to_portal(dt.EMAIL_USERNAME, dt.EMAIL_PASSWORD)
        with allure.step("Go to Suppliers page"):
            menu_page.go_to_option(st.SUPPLIERS_TEXT)
            suppliers_page.go_to_supplier_by_name(supplier)
        with allure.step("Verify supplier acc"):
            assert supplier_details.check_accounts_are_present(supp_acc)

    def test_create_product_configuration(self, my_app):
        with allure.step("Pages init"):
            login_page = Login(my_app)
            menu_page = Menu(my_app)
            suppliers_page = Suppliers(my_app)
            supplier_details = SupplierDetails(my_app)
        with allure.step("Login to portal"):
            login_page.login_to_portal(dt.EMAIL_USERNAME, dt.EMAIL_PASSWORD)
        with allure.step("Go to Suppliers page"):
            menu_page.go_to_option(st.SUPPLIERS_TEXT)
            suppliers_page.go_to_supplier_by_name(dt.SUPPLIER_NAME_CY_SEND)
        with allure.step("Delete product config"):
            supplier_details.delete_product_config(dt.PRODUCT_CONFIG_ID_CASE_1)
        with allure.step("Add product config"):
            add_prod_config = supplier_details.create_product_config()
            add_prod_config.create_configuration(conf_id=dt.PRODUCT_CONFIG_ID_CASE_1,
                                                 currency=dt.PRODUCT_CONFIG_PRODUCT_CURRENCY_CASE_1,
                                                 region=dt.PRODUCT_CONFIG_COUNTRY_CASE_1,
                                                 face_value=dt.PRODUCT_CONFIG_FACE_VALUE_CASE_1,
                                                 supp_price=dt.PRODUCT_CONFIG_SUPPLIER_PRICE_CASE_1,
                                                 price_currency=dt.PRODUCT_CONFIG_PRICE_CURRENCY_CASE_1,
                                                 vat_value=dt.PRODUCT_CONFIG_VAT_VALUE_CASE_1)
            supplier_details.reload_page()
        with allure.step("Verify product config info"):
            assert supplier_details.check_product_config_details(config_id=dt.PRODUCT_CONFIG_ID_CASE_1,
                                                                 exp_country=dt.PRODUCT_CONFIG_COUNTRY_CASE_1,
                                                                 exp_face_value=dt.PRODUCT_CONFIG_FACE_VALUE_CASE_1,
                                                                 exp_currency=dt.PRODUCT_CONFIG_PRODUCT_CURRENCY_CASE_1,
                                                                 exp_supp_price=dt.PRODUCT_CONFIG_SUPPLIER_PRICE_CASE_1,
                                                                 exp_price_currency=dt.PRODUCT_CONFIG_PRICE_CURRENCY_CASE_1)
