from Pages.Brands.BrandsPage import Brands
from Pages.LoginPage import Login
from Pages.MenuPage import Menu
from Constants import Data as dt
from Constants import SearchText as st
from Constants import ExpectedResults as exp


class TestBrands:

    def test_filters(self, my_app):
        brand_page = Brands(my_app)
        login_page = Login(my_app)
        menu_page = Menu(my_app)

        # Login to portal
        login_page.login_to_portal(dt.EMAIL_USERNAME, dt.EMAIL_PASSWORD)
        # Go to Brand page
        menu_page.expand_options(st.PRODUCTS_TEXT)
        menu_page.go_to_option(st.BRANDS_TEXT)
        # Apply filters
        brand_page.filter_brand_by_region(st.REGION_CASE_1)
        brand_page.filter_brands_by_currency(st.CURRENCY_CASE_1)
        brand_page.filter_brands_by_supplier(st.SUPPLIER_CASE_1)
        brand_page.filter_brand_by_integration(st.INTEGRATION_CASE_1)
        brand_page.filter_brand_by_brand(st.BRAND_CASE_1)
        # Verify brand is correct
        assert brand_page.check_filter_result_much(exp.EXPECTED_BRAND_NAME_1)

    def test_create_new_brand(self, my_app):
        brand_page = Brands(my_app)
        login_page = Login(my_app)
        menu_page = Menu(my_app)

        # Login to portal
        login_page.login_to_portal(dt.EMAIL_USERNAME, dt.EMAIL_PASSWORD)
        # Go to Brand page
        menu_page.expand_options(st.PRODUCTS_TEXT)
        menu_page.go_to_option(st.BRANDS_TEXT)
        # Go to create new brand popup
        new_brand_popup = brand_page.go_to_create_brand()
        new_brand_popup.create_new_brand(name=dt.BRAND_NAME_1, region=dt.BRAND_REGION_1, currency=dt.BRAND_CURRENCY_1,
                                         description=dt.BRAND_DESCRIPTION_1)
        brand_details = brand_page.find_brand_with_search_field(dt.BRAND_NAME_1)
        assert brand_details.check_brands_info(exp.EXPECTED_BRAND_CURRENCY_2, exp.EXPECTED_BRAND_REGION_2,
                                               exp.EXPECTED_BRAND_SUPPLIER_2)
