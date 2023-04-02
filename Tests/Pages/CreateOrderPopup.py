from Tests.BaseWrapper.Driver import DriverWrapper
from Tests.Pages.ShoppingCards.CheckoutBasketPage import CheckoutBasket


class CreateOrder(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    CLIENT_DROPDOWN_CSS = 'input[placeholder="Client"]'
    ACCOUNT_DROPDOWN_CSS = 'input[placeholder="Account"]'
    BRANDS_DROPDOWN_CSS = 'input[placeholder="Brand"]'
    SUPPLIER_NAME_XPATH = '//div[contains(text(), "Supplier")]/following-sibling::div[1]'
    CURRENCY_NAME_XPATH = '//div[contains(text(), "Currency")]/following-sibling::div[1]'
    PRODUCT_ROW_DENOMINATION_XPATH = '//tr[{0}]/td[2]//input'
    PRODUCT_ROW = '//td[1]/p'
    PRODUCTS_QUANTITY_XPATH = '//tr[{0}]/td[3]//input'
    OVERWRITE_PRICE_INPUT_XPATH = '//tr[{0}]/td[7]//input'
    DISCOUNT_INPUT_XPATH = '//tr[{0}]/td[8]//input'
    ADD_TO_CARD_BUTTON_TEXT = 'Add to cart'
    ADD_TO_CARD_AND_CHECKOUT_BUTTON_CSS_TEXT = 'Add to cart and checkout'

    def find_products_row(self, product_name):
        rows = self.search_elements_by_xpath(self.PRODUCT_ROW)
        index = 0
        for row in rows:
            index += 1
            if row.text == product_name:
                return index

    def set_client(self, client):
        self.dropdown_input_css(self.CLIENT_DROPDOWN_CSS, client)

    def set_account(self, account):
        self.dropdown_input_css(self.ACCOUNT_DROPDOWN_CSS, account)

    def set_brand(self, brand):
        self.dropdown_input_css(self.BRANDS_DROPDOWN_CSS, brand)

    def set_denomination(self, product, denomination):
        input_field = self.search_element_by_xpath(self.PRODUCT_ROW_DENOMINATION_XPATH.format(product))
        self.input_in_element(input_field, denomination)

    def set_quantity(self, product, quantity):
        row_num = self.find_products_row(product)
        input_field = self.search_element_by_xpath(self.PRODUCTS_QUANTITY_XPATH.format(row_num))
        self.input_in_element(input_field, quantity)

    def overwrite_price(self, product, price):
        input_field = self.search_element_by_xpath(self.OVERWRITE_PRICE_INPUT_XPATH.format(product))
        self.input_in_element(input_field, price)

    def set_discount(self, product, discount):
        input_field = self.search_element_by_xpath(self.DISCOUNT_INPUT_XPATH.format(product))
        self.input_in_element(input_field, discount)

    def click_add_to_card(self):
        button = self.search_element_by_text('span', self.ADD_TO_CARD_BUTTON_TEXT)
        button.find_element_by_xpath('..').click()

    def click_add_to_card_and_checkout(self):
        button = self.search_element_by_text('span', self.ADD_TO_CARD_AND_CHECKOUT_BUTTON_CSS_TEXT)
        button.find_element_by_xpath('..').click()
        shopping_card = CheckoutBasket(self.driver)
        return shopping_card



