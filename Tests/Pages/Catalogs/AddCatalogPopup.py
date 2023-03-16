from Tests.BaseWrapper.Driver import DriverWrapper


class AddCatalog(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    CATALOG_NAME_INPUT_FIELD_NAME = 'name'
    DESCRIPTION_INPUT_FIELD_NAME = 'description'
    TRANSACTION_FEE_FIELD_NAME = 'transactionFeeValue'
    SUPPLIER_FEE_FIELD_NAME = 'supplierPriceFeeValue'
    FEE_SWITCH_INPUT_NAME = 'transactionFeeTypeSwitch'
    DISCOUNT_SWITCH_INPUT_NAME = 'clientDiscountTypeSwitch'
    DISCOUNT_TYPE_DROPDOWN_CSS = 'input[placeholder="Discount type"]'
    DISCOUNT_VALUE_INPUT_NAME = 'clientDiscountValue'
    SAVE_CATALOG_BUTTON_CSS = 'button[type="submit"]'

    def set_name(self, name):
        self.input_in_search_field_name(self.CATALOG_NAME_INPUT_FIELD_NAME, name)

    def set_description(self, description):
        self.input_in_search_field_name(self.DESCRIPTION_INPUT_FIELD_NAME, description)

    def turn_on_fee(self):
        switch = self.search_element_by_name(self.FEE_SWITCH_INPUT_NAME)
        switch.click()

    def turn_on_discount(self):
        switch = self.search_element_by_name(self.DISCOUNT_SWITCH_INPUT_NAME)
        switch.click()

    def set_transaction_fee(self, fee):
        self.input_in_search_field_name(self.TRANSACTION_FEE_FIELD_NAME, fee)

    def set_supplier_fee(self, fee):
        self.input_in_search_field_name(self.SUPPLIER_FEE_FIELD_NAME, fee)
