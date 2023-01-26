from Tests.BaseWrapper.Driver import DriverWrapper


class Suppliers(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    SEARCH_FIELD_NAME = 'searchText'
    CURRENCY_FILTER_CSS = 'input[placeholder="Currency"]'
    TAG_FOR_SUPPLIER_ROW = 'tbody/tr/td:nth-child(1)'

    def go_to_supplier_with_search(self, search_text):
        self.input_in_search_field_name(self.SEARCH_FIELD_NAME, search_text)
        self.search_element_by_xpath('//' + self.TAG_FOR_SUPPLIER_ROW).click()

    def go_to_supplier_by_name(self, supplier_name):
        supplier = self.search_element_by_text(self.TAG_FOR_SUPPLIER_ROW, supplier_name)
        self.scroll_to_the_element(supplier)
        supplier.click()

    def filter_suppliers_by_currency(self, currency):
        self.dropdown_input_css(self.CURRENCY_FILTER_CSS, currency)

    def check_supplier_list(self, exp_suppliers):
        supplier_list = self.search_elements_by_xpath('//' + self.TAG_FOR_SUPPLIER_ROW)
        suppliers_names = []
        for sup in supplier_list:
            suppliers_names.append(sup.text)
        if suppliers_names == exp_suppliers:
            return True
        else:
            return False

    def check_supplier_is_present(self, sup_name):
        supplier_list = self.search_elements_by_xpath('//' + self.TAG_FOR_SUPPLIER_ROW)
        suppliers_names = []
        for sup in supplier_list:
            suppliers_names.append(sup.text)
        if sup_name in suppliers_names:
            return True
        else:
            return False
