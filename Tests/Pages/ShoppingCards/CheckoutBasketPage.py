import time

from Tests.BaseWrapper.Driver import DriverWrapper
from Tests.Pages.OrderHistory.OrderDetailsPage import OrderDetails
from Tests.Pages.OrderHistory.OrderHistoryPage import OrderHistory


class CheckoutBasket(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    PRODUCT_ROW_XPATH = '//td//p[2]'
    QUANTITY_INPUT_CSS = 'tr:nth-child({0}) input[type="tel"]'
    COMMENT_INPUT_FIELD_CSS = 'input[placeholder="Comment"]'
    CHECKOUT_BUTTON_TEXT = 'Checkout'
    ADD_COMMENT_BUTTON = 'Add comment'
    ERASE_TEXT_BUTTON = 'Erase text'
    DELETE_PRODUCT_BUTTON_XPATH = 'tr:nth-child({0})>td:nth-child(8)>button'
    CONFIRMATION_POPUP = '.MuiPaper-elevation1.MuiPaper-rounded'
    CONFIRM_BUTTON = f'{CONFIRMATION_POPUP} button.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton' \
                     f'-containedPrimary.MuiButton-containedSizeLarge.MuiButton-sizeLarge'

    def find_basket_row(self, product_text):
        products = self.search_elements_by_xpath(self.PRODUCT_ROW_XPATH)
        row_num = 0
        for product in products:
            row_num += 1
            if product.text == product_text:
                break
        return str(row_num)

    def change_quantity(self, product, quantity):
        self.input_in_search_field_css(self.QUANTITY_INPUT_CSS.format(self.find_basket_row(product)), quantity)

    def delete_product_from_basket(self, product):
        delete_button = self.search_element_by_xpath(self.DELETE_PRODUCT_BUTTON_XPATH.format(product))
        delete_button.click()

    def checkout_basket(self):
        checkout_button = self.search_element_by_text('span', self.CHECKOUT_BUTTON_TEXT)
        button = checkout_button.find_element_by_xpath('..')
        button.click()
        time.sleep(2)
        self.click_the_button_css(self.CONFIRM_BUTTON)
        order_history_page = OrderDetails(self.driver)
        return order_history_page

    def input_comment(self, comment):
        self.input_in_search_field_css(self.COMMENT_INPUT_FIELD_CSS, comment)

    def click_add_comment(self):
        add_comment = self.search_element_by_text('span', self.ADD_COMMENT_BUTTON)
        add_comment.find_element_by_xpath('..').click()

    def add_comment(self, comment):
        self.input_comment(comment)
        self.click_add_comment()


