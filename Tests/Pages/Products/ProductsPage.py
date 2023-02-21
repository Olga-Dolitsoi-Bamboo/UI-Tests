from Tests.BaseWrapper.Driver import DriverWrapper
from Tests.Pages.Products.IProductsTab import IntegratedProducts


class Products(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    INTEGRATED_PRODUCTS_TAB = 'button[tabindex="0"]'
    NON_INTEGRATED_PRODUCTS_TAB = 'button[tabindex="1"]'
    SUPPLIERS_DROPDOWN_CSS = 'div[placeholder = "All Suppliers"]>div>div>input'
    REGIONS_DROPDOWN_CSS = 'div[placeholder = "All Regions"]>div>div>input'
    CURRENCIES_DROPDOWN_CSS = 'div[placeholder = "All Currencies"]>div>div>input'
    BRANDS_DROPDOWN_CSS = 'div[placeholder = "All Brands"]>div>div>input'
    DENOMINATION_INPUT_NAME = '[name="denomination"]'
    ADD_TO_CATALOG_XPATH = '//td[@value="{0}"][2]//svg'
    ADD_BRAND_TO_CATALOG_XPATH = '//td[@value="{0}"][1]//svg'

    def go_to_integrated_tab(self):
        integrated_tab = self.search_element_by_css(self.INTEGRATED_PRODUCTS_TAB)
        is_selected = integrated_tab.get_attribute("aria-selected")
        if is_selected == "false":
            integrated_tab.click()
            integrated_page = IntegratedProducts(self.driver)
            return integrated_page

    def go_to_non_integrated_tab(self):
        non_integrated_tab = self.search_element_by_css(self.INTEGRATED_PRODUCTS_TAB)
        is_selected = non_integrated_tab.get_attribute("aria-selected")
        if is_selected == "false":
            non_integrated_tab.click()
            non_integrated_page = IntegratedProducts(self.driver)
            return non_integrated_page

    def filter_products_by_suppliers(self, supplier_name):
        self.dropdown_input_css(self.SUPPLIERS_DROPDOWN_CSS, supplier_name)

    def filter_products_by_region(self, region):
        self.dropdown_input_css(self.REGIONS_DROPDOWN_CSS, region)

    def filter_products_by_currency(self, currency):
        self.dropdown_input_css(self.CURRENCIES_DROPDOWN_CSS, currency)

    def filter_products_by_brand(self, brand):
        self.dropdown_input_css(self.BRANDS_DROPDOWN_CSS, brand)

    def filter_products_by_denomination(self, denomination):
        self.input_in_search_field_name(self.DENOMINATION_INPUT_NAME, denomination)

    def go_to_add_brand_to_catalog(self, brand_name):
        button = self.search_element_by_xpath(self.ADD_BRAND_TO_CATALOG_XPATH.format(brand_name))
        button.click()

    def go_to_add_product_to_catalog(self, product_name):
        button = self.search_element_by_xpath(self.ADD_TO_CATALOG_XPATH.format(product_name))
        button.click()
