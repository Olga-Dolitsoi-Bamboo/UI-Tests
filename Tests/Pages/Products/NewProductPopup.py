from Tests.BaseWrapper.Driver import DriverWrapper


class NewProduct(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    PRODUCT_NAME_INPUT_NAME = 'name'
    DENOMINATION_INPUT_NAME = 'faceValue'
    SKU_INPUT_NAME = 'sku'
    SUPPLIER_CURRENCY_DROPDOWN_CSS = 'div[name="supplierCurrencyCode"]>div>div>input'
    BRAND_DROPDOWN_CSS = 'div[name="brandId"]>div>div>input'
    CONFIRM_BUTTON_CSS = 'button[type="submit"]'

    def set_name(self, name):
        self.input_in_search_field_name(self.PRODUCT_NAME_INPUT_NAME, name)

    def set_denomination(self, denomination):
        self.input_in_search_field_name(self.DENOMINATION_INPUT_NAME, denomination)

    def set_sku(self, sku):
        self.input_in_search_field_name(self.SKU_INPUT_NAME, sku)

    def set_supplier_currency(self, currency):
        self.dropdown_input_css(self.SUPPLIER_CURRENCY_DROPDOWN_CSS, currency)

    def set_brand(self, brand):
        self.dropdown_input_css(self.BRAND_DROPDOWN_CSS, brand)

    def create_new_product(self, name, denomination, sku, currency, brand):
        self.set_name(name)
        self.set_denomination(denomination)
        self.set_sku(sku)
        self.set_supplier_currency(currency)
        self.set_brand(brand)
        self.click_the_button_css(self.CONFIRM_BUTTON_CSS)


