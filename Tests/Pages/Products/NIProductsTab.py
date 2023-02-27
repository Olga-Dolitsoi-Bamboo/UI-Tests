from Tests.BaseWrapper.Driver import DriverWrapper
from Tests.Pages.Products.NewProductPopup import NewProduct


class NonIntegratedProducts(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    UPLOAD_CODES_BUTTON_TEXT = 'Upload codes'
    ADD_NEW_BRAND_BUTTON_TEXT = 'Add new brand'
    EXPORT_EXCEL_BUTTON_TEXT = 'Export Excel'
    EDIT_PRODUCTS_BUTTON_TEXT = 'Edit Products'
    ADD_PRODUCTS_BUTTON_TEXT = 'Add products'
    PRODUCT_SKU_XPATH = '//td[contains(text(), "{0}")]'
    ATTRIBUTE_BY_SKU_XPATH = '//td[contains(text(), "{0}")]/following-sibling::td[{1}]'
    BRAND_COLUMN_NUMBER = '1'
    NAME_COLUMN_NUMBER = '2'
    CURRENCY_COLUMN_NUMBER = '5'
    DENOMINATION_COLUMN_NUMBER = '6'
    PRODUCT_SELECT_FLAG_XPATH = '//td[contains(text(), "{0}")]/preceding-sibling::td[1]//input'
    ACTIONS_WITH_PRODUCTS_TEXT = 'Actions with products'
    ACTIVATE_SELECTED_BUTTON_TEXT = 'Activate selected'
    DEACTIVATE_SELECTED_BUTTON_TEXT = 'Deactivate selected'
    RESTORE_SELECTED_BUTTON_TEXT = 'Restore selected'
    DELETE_SELECTED_BUTTON_TEXT = 'Delete selected'

    def click_upload_codes(self):
        button = self.search_element_by_text('span', self.UPLOAD_CODES_BUTTON_TEXT)
        button.find_element_by_xpath('..').click()

    def click_add_new_brand_button(self):
        button = self.search_element_by_text('span', self.ADD_NEW_BRAND_BUTTON_TEXT)
        button.find_element_by_xpath('..').click()

    def click_export_excel_button(self):
        button = self.search_element_by_text('span', self.EXPORT_EXCEL_BUTTON_TEXT)
        button.find_element_by_xpath('..').click()

    def click_edit_products_button(self):
        button = self.search_element_by_text('span', self.EDIT_PRODUCTS_BUTTON_TEXT)
        button.find_element_by_xpath('..').click()

    def select_product_checkbox(self, name):
        self.search_element_by_xpath(self.PRODUCT_SELECT_FLAG_XPATH.format(name)).click()

    def click_actions_button(self):
        self.search_element_by_text('div', self.ACTIONS_WITH_PRODUCTS_TEXT).click()

    def click_activate_button(self):
        self.search_element_by_text('li', self.ACTIVATE_SELECTED_BUTTON_TEXT).click()

    def click_deactivate_button(self):
        self.search_element_by_text('li', self.DEACTIVATE_SELECTED_BUTTON_TEXT).click()

    def click_restore_button(self):
        self.search_element_by_text('li', self.RESTORE_SELECTED_BUTTON_TEXT).click()

    def click_delete_button(self):
        self.search_element_by_text('li', self.DELETE_SELECTED_BUTTON_TEXT).click()

    def click_add_product_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        button = self.search_element_by_text('span', self.ADD_PRODUCTS_BUTTON_TEXT)
        button.find_element_by_xpath('..').click()
        add_product_popup = NewProduct(self.driver)
        return add_product_popup

    def verify_product_info(self, exp_name, exp_denomination, exp_sku, exp_currency, exp_brand):
        result = self.check_is_present_xpath(self.PRODUCT_SKU_XPATH.format(exp_sku))
        brand = self.search_element_by_xpath(self.ATTRIBUTE_BY_SKU_XPATH.format(exp_sku, self.BRAND_COLUMN_NUMBER)).text
        name = self.search_element_by_xpath(self.ATTRIBUTE_BY_SKU_XPATH.format(exp_sku, self.NAME_COLUMN_NUMBER)).text
        currency = self.search_element_by_xpath(self.ATTRIBUTE_BY_SKU_XPATH.format(exp_sku,
                                                                                   self.CURRENCY_COLUMN_NUMBER)).text
        denomination = self.search_element_by_xpath(self.ATTRIBUTE_BY_SKU_XPATH.format(
            exp_sku, self.DENOMINATION_COLUMN_NUMBER)).text
        if result and exp_name == name and exp_denomination == denomination and exp_currency == currency and exp_brand == brand:
            return True
        else:
            return False



