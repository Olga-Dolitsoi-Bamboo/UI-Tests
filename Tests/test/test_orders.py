import allure

from Tests.Pages.LoginPage import Login
from Tests.Pages.MenuPage import Menu
from Tests.Constants import Data as dt
from Tests.Constants import SearchText as st
from Tests.Pages.CreateOrderPopup import CreateOrder


class TestClassOrders:
    def test_user_can_create_order(self, my_app):
        with allure.step("Pages init"):
            login_page = Login(my_app)
            menu_page = Menu(my_app)
            new_order = CreateOrder(my_app)

        with allure.step("Login to portal"):
            login_page.login_to_portal(dt.EMAIL_USERNAME, dt.EMAIL_PASSWORD)
        with allure.step("Go to Brand page"):
            menu_page.expand_options(st.ORDERS_TEXT)
            menu_page.go_to_option(st.NEW_ORDER_TEXT)
        with allure.step("Set client"):
            new_order.set_client(dt.CLIENT_FOR_ORDERS)
        with allure.step("Set account"):
            new_order.set_account(dt.ACCOUNT_FOR_ORDERS)
        with allure.step("Select brand"):
            new_order.set_brand(dt.BRAND_FOR_ORDERS)
        with allure.step("Set quantity"):
            new_order.set_quantity(dt.PRODUCT_FOR_ORDERS, dt.QUANTITY_FOR_ORDERS)
        with allure.step("Go to basket"):
            basket = new_order.click_add_to_card_and_checkout()
        with allure.step("Checkout order"):
            order_details = basket.checkout_basket()
        with allure.step("Check order status"):
            assert order_details.check_status()



