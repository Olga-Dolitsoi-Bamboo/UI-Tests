from Tests.Pages.LoginPage import Login
from Tests.Pages.MenuPage import Menu
from Tests.Pages.Products.ProductsPage import Products
from Tests.Constants import Data as dt
from Tests.Constants import SearchText as st


class TestClassProducts:
    def test_add_ni_product(self, my_app):
        login_page = Login(my_app)
        menu_page = Menu(my_app)
        product_page = Products(my_app)

        # Login to portal
        login_page.login_to_portal(dt.EMAIL_USERNAME, dt.EMAIL_PASSWORD)
        # Go to Brand page
        menu_page.expand_options(st.PRODUCTS_TEXT)
        menu_page.go_to_option(st.PRODUCT_LIST_TEXT)
        ni_tab = product_page.go_to_non_integrated_tab()
        add_product_popup = ni_tab.click_add_product_button()
        add_product_popup.create_new_product(dt.NI_PRODUCT_NAME_CASE_1, dt.NI_PRODUCT_DENOMINATION_CASE_1,
                                             dt.NI_PRODUCT_SKU_CASE_1, dt.NI_PRODUCT_CURRENCY_CASE_1,
                                             dt.NI_PRODUCT_BRAND_CASE_1)
        assert ni_tab.verify_product_info(dt.NI_PRODUCT_NAME_CASE_1, dt.NI_PRODUCT_DENOMINATION_CASE_1,
                                          dt.NI_PRODUCT_SKU_CASE_1, dt.NI_PRODUCT_CURRENCY_CASE_1,
                                          dt.NI_PRODUCT_BRAND_CASE_1)

