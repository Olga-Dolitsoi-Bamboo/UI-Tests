from Tests.Pages.Brands.BrandsPage import Brands
from Tests.Pages.LoginPage import Login
from Tests.Pages.MenuPage import Menu
from Tests.Constants import Data as dt
from Tests.Constants import SearchText as st
from Tests.Constants import ExpectedResults as exp


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

