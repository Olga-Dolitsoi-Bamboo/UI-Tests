from Tests.BaseWrapper.Driver import DriverWrapper


class CreateNewBrand(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    BRAND_NAME_INPUT_NAME = 'brandName'
    REGION_DROPDOWN_CSS = 'div[name="integrationType"]>div>div>input'
    CURRENCY_DROPDOWN_CSS = 'div[name="integrationType"]>div>div>input'
    XERO_DROPDOWN_CSS = 'div[name="integrationType"]>div>div>input'
    DESCRIPTION_INPUT_CSS = '//label[contains(text(), "{1}")]/following:div/textarea'
    TERMS_INPUT_CSS = '//label[contains(text(), "{1}")]/following:div/textarea'
    INSTRUCTION_INPUT_CSS = '//label[contains(text(), "{1}")]/following:div/textarea'
    LIVE_STATUS_SWITCHER_CSS = ''
    URL_BRAND_SWITCHER_CSS = ''
    SAVE_NEW_BRAND_CSS = 'button[type="submit"]'

    def fill_brand_info(self, name, region, currency, xero='', description='', terms='', instruction=''):
        self.input_in_search_field_name(self.BRAND_NAME_INPUT_NAME, name)
        self.dropdown_input_css(self.REGION_DROPDOWN_CSS, region)
        self.dropdown_input_css(self.CURRENCY_DROPDOWN_CSS, currency)
        if xero != '':
            self.dropdown_input_css(self.XERO_DROPDOWN_CSS, xero)
        if description != '':
            self.input_in_search_field_css(self.DESCRIPTION_INPUT_CSS, description)
        if terms != '':
            self.input_in_search_field_css(self.TERMS_INPUT_CSS, terms)
        if instruction != '':
            self.input_in_search_field_css(self.INSTRUCTION_INPUT_CSS, instruction)

    def set_statuses(self, live_satus=True, url_brand=True):
        if not live_satus:
            self.click_the_button_css(self.LIVE_STATUS_SWITCHER_CSS)
        if not url_brand:
            self.click_the_button_css(self.URL_BRAND_SWITCHER_CSS)

    def create_new_brand(self, name, region, currency, xero='', description='', terms='', instruction='',
                         live_satus=True, url_brand=True):
        self.fill_brand_info(name, region, currency, xero, description, terms, instruction)
        self.set_statuses(live_satus, url_brand)
        submit = self.search_element_by_css(self.SAVE_NEW_BRAND_CSS)
        self.scroll_to_the_element(submit)
        submit.click()




