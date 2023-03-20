from Tests.BaseWrapper.Driver import DriverWrapper


class ShoppingCards(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    BRAND_FILTER_DROPDOWN_CSS = 'input[placeholder="Brand"]'
    CLIENT_FILTER_DROPDOWN_CSS = 'input[placeholder="Client"]'
    CURRENCY_FILTER_DROPDOWN_CSS = 'input[placeholder="Total Value Currency"]'
    BASKET_ROW_CSS = 'td[value="{0}"]'
    DELETE_BASKET_XPATH = '//td[contains(text(), "{0}")]/following-sibling::td[5]'

    def filter_cards_by_brand(self, brand):
        self.dropdown_input_css(self.BRAND_FILTER_DROPDOWN_CSS, brand)

    def filter_cards_by_client(self, client):
        self.dropdown_input_css(self.CLIENT_FILTER_DROPDOWN_CSS, client)

    def filter_cards_by_currency(self, currency):
        self.dropdown_input_css(self.CURRENCY_FILTER_DROPDOWN_CSS, currency)

    def go_to_card(self, card_name):
        self.search_element_by_css(self.BASKET_ROW_CSS.format(card_name))

    def delete_basket(self, card_name):
        basket = self.search_element_by_xpath(self.DELETE_BASKET_XPATH.format(card_name))
        basket.click()

