import time

from Tests.BaseWrapper.Driver import DriverWrapper


class OrderDetails(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    NUM_OF_CARDS_CSS = 'span[title="Total number of cards in the order"]'
    NUM_OF_SUCCESSFUL_CARDS_CSS = 'span[title="Number of successful cards"]'
    NUM_OF_FAILED_CARDS_CSS = 'span[title="Number of failed cards"]'
    NUM_OF_OTHER_STATUSES_CARDS_CSS = 'span[title="Number of cards with other status"]'
    ORDER_INFO_EXPAND_AREA_CSS = '.MuiButtonBase-root.MuiAccordionSummary-root'
    SEND_INVOICE_BUTTON = 'Send Invoice'
    DOWNLOAD_INVOICE_BUTTON = 'Download Invoice'
    DOWNLOAD_CLIENT_EXCEL = 'Download admin excel'
    DOWNLOAD_ADMIN_EXCEL = 'Download client excel'
    REFUND_DROPDOWN = 'Refund'
    FULL_REFUND_OPTION = 'li[data-value="fullRefund"]'
    PARTIAL_REFUND_OPTION = 'li[data-value="partialRefund"]'
    CARD_STATUS_COLUMN = '3'
    PRODUCT_NAME_COLUMN = '5'

    def see_sold_cards(self):
        span = self.search_element_by_css(self.NUM_OF_SUCCESSFUL_CARDS_CSS)
        button = span.find_element_by_xpath('..')
        button.click()

    def expand_order_details(self):
        self.click_the_button_css(self.ORDER_INFO_EXPAND_AREA_CSS)

    def check_status(self):
        time.sleep(5)
        self.driver.refresh()
        self.expand_order_details()
        if self.check_is_present_text('span', 'Succeeded'):
            return True






