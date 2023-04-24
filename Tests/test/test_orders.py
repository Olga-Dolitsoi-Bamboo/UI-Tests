from Pages.LoginPage import Login
from Pages.MenuPage import Menu
from Constants import Data as dt
from Constants import SearchText as st
from Pages.CreateOrderPopup import CreateOrder


class TestClassOrders:
    def test_user_can_create_order(self, my_app):
        login_page = Login(my_app)
        menu_page = Menu(my_app)
        new_order = CreateOrder(my_app)

        login_page.login_to_portal(dt.EMAIL_USERNAME, dt.EMAIL_PASSWORD)
        # Go to Brand page
        menu_page.expand_options(st.ORDERS_TEXT)
        menu_page.go_to_option(st.NEW_ORDER_TEXT)
        new_order.set_client(dt.CLIENT_FOR_ORDERS)
        new_order.set_account(dt.ACCOUNT_FOR_ORDERS)
        new_order.set_brand(dt.BRAND_FOR_ORDERS)
        new_order.set_quantity(dt.PRODUCT_FOR_ORDERS, dt.QUANTITY_FOR_ORDERS)
        basket = new_order.click_add_to_card_and_checkout()
        order_details = basket.checkout_basket()
        assert order_details.check_status()



