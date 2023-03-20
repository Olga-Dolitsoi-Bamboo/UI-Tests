from Tests.BaseWrapper.Driver import DriverWrapper


class AddCatalog(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    CREATE_CATALOG_POPUP = '.MuiPaper-elevation1.MuiPaper-rounded'
    CATALOG_NAME_INPUT_FIELD_NAME = 'name'
    DESCRIPTION_INPUT_FIELD_NAME = 'description'
    TRANSACTION_FEE_FIELD_NAME = 'transactionFeeValue'
    SUPPLIER_FEE_FIELD_NAME = 'supplierPriceFeeValue'
    FEE_SWITCH_INPUT_NAME = 'transactionFeeTypeSwitch'
    DISCOUNT_SWITCH_INPUT_NAME = 'clientDiscountTypeSwitch'
    DISCOUNT_TYPE_DROPDOWN_CSS = 'input[placeholder="Discount type"]'
    DISCOUNT_VALUE_INPUT_NAME = 'clientDiscountValue'
    SAVE_CATALOG_BUTTON_XPATH = '//span[contains(text(), "Save new catalog")]'

    def set_name(self, name):
        self.input_in_search_field_name(self.CATALOG_NAME_INPUT_FIELD_NAME, name)

    def set_description(self, description):
        popup = self.search_element_by_css(self.CREATE_CATALOG_POPUP)
        field = popup.find_element_by_name(self.DESCRIPTION_INPUT_FIELD_NAME)
        self.input_into_element(field, description)

    def turn_on_fee(self):
        popup = self.search_element_by_css(self.CREATE_CATALOG_POPUP)
        switch = popup.find_element_by_name(self.FEE_SWITCH_INPUT_NAME)
        switch.click()

    def turn_on_discount(self):
        popup = self.search_element_by_css(self.CREATE_CATALOG_POPUP)
        switch = popup.find_element_by_name(self.DISCOUNT_SWITCH_INPUT_NAME)
        switch.click()

    def set_transaction_fee(self, fee):
        self.input_in_search_field_name(self.TRANSACTION_FEE_FIELD_NAME, fee)

    def set_supplier_fee(self, fee):
        self.input_in_search_field_name(self.SUPPLIER_FEE_FIELD_NAME, fee)

    def set_discount(self, discount):
        self.input_in_search_field_name(self.DISCOUNT_VALUE_INPUT_NAME, discount)

    def click_save_button(self):
        popup = self.search_element_by_css(self.CREATE_CATALOG_POPUP)
        button = popup.find_element_by_xpath(self.SAVE_CATALOG_BUTTON_XPATH)
        button.find_element_by_xpath('..').click()

    def create_catalog(self, name, discount, description='', supplier_fee='', transaction_fee=''):
        self.set_name(name)
        self.turn_on_discount()
        self.set_discount(discount)
        if description != '':
            self.set_description(description)
        if supplier_fee != '' or transaction_fee != '':
            self.turn_on_fee()
            if supplier_fee != '':
                self.set_supplier_fee(supplier_fee)
            if transaction_fee != '':
                self.set_transaction_fee(transaction_fee)
        self.click_save_button()
