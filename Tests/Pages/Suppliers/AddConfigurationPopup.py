from Tests.BaseWrapper.Driver import DriverWrapper


class AddConfiguration(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    CONFIG_ID_INPUT_NAME = 'supplierProductCode'
    REGION_DROPDOWN_CSS = 'div[name="countryCode"]>div>div>input'
    FACE_VALUE_INPUT_NAME = 'faceValue'
    CURRENCY_DROPDOWN_CSS = 'div[name="currencyCode"]>div>div>input'
    SUPPLIER_PRICE_INPUT_NAME = 'supplierPrice'
    PRICE_CURRENCY_DROPDOWN_CSS = 'div[name="supplierPriceCurrencyCode"]>div>div>input'
    VAT_TYPE_DROPDOWN_CSS = 'div[name="vatType"]>div>div>input'
    VAT_VALUE_INPUT_NAME = 'vatValue'
    ADD_CONFIGURATION_POPUP = '.MuiDialog-paper'
    ADD_ASSIGNMENT_BUTTON = f'{ADD_CONFIGURATION_POPUP} .MuiButtonBase-root.MuiButton-root.MuiButton-contained' \
                            f'.MuiButton-containedPrimary.MuiButton-containedSizeLarge.MuiButton-sizeLarge'

    def create_configuration(self, conf_id, region, face_value, currency, supp_price, price_currency,
                             vat_type, vat_value):
        self.input_in_search_field_name(self.CONFIG_ID_INPUT_NAME, conf_id)
        self.dropdown_input_css(self.REGION_DROPDOWN_CSS, region)
        self.input_in_search_field_name(self.FACE_VALUE_INPUT_NAME, face_value)
        self.dropdown_input_css(self.CURRENCY_DROPDOWN_CSS, currency)
        self.input_in_search_field_name(self.SUPPLIER_PRICE_INPUT_NAME, supp_price)
        self.dropdown_input_css(self.PRICE_CURRENCY_DROPDOWN_CSS, price_currency)
        self.dropdown_input_css(self.VAT_TYPE_DROPDOWN_CSS, vat_type)
        self.input_in_search_field_name(self.VAT_VALUE_INPUT_NAME, vat_value)
        self.click_the_button_css(self.ADD_ASSIGNMENT_BUTTON)
