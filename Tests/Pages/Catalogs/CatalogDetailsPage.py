from Tests.BaseWrapper.Driver import DriverWrapper


class CatalogDetails(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    DOWNLOAD_PRICE_LIST_BUTTON_TEXT = 'Download price list'
    DOWNLOAD_CLIENT_PRICE_LIST_TEXT = 'Download client price list'
    CREATE_ORDER_BUTTON_TEXT = 'Create order'
    SEARCH_INPUT_FIELD_NAME = 'searchText'
    DENOMINATION_INPUT_FIELD_NAME = 'denomination'
    SUPPLIERS_FILTER_DROPDOWN_CSS = '[placeholder="All Suppliers"]'
    REGIONS_FILTER_DROPDOWN_CSS = '[placeholder="All Regions"]'
    CURRENCIES_FILTER_DROPDOWN_CSS = '[placeholder="All Currencies"]'
    BRANDS_FILTER_DROPDOWN_CSS = '[placeholder="All Brands"]'
    TREE_DOTS_BUTTON_CSS = '.MuiTabs-scroller.MuiTabs-fixed svg'
    ADD_ALL_PRODUCTS_OPTION_TEXT = 'Add all products'
    DUPLICATE_CATALOG_TEXT = 'Duplicate'
    EDIT_CATALOG_TEXT = 'Edit'
    DELETE_CATALOG_TEXT = 'Delete'
    ACTIVE_PRODUCTS_TAB_TEXT = 'Active'
    INACTIVE_PRODUCTS_TAB_TEXT = 'Inactive'
    CLIENTS_TAB_TEXT = 'Clients'

    def go_to_active_products(self):
        tab = self.search_element_by_text('span', self.ACTIVE_PRODUCTS_TAB_TEXT)
        button = tab.find_element_by_xpath('..')
        button.click()

    def go_to_inactive_products(self):
        tab = self.search_element_by_text('span', self.INACTIVE_PRODUCTS_TAB_TEXT)
        button = tab.find_element_by_xpath('..')
        button.click()

    def go_to_clients_tab(self):
        tab = self.search_element_by_text('span', self.CLIENTS_TAB_TEXT)
        button = tab.find_element_by_xpath('..')
        button.click()

    def duplicate_catalog(self):
        button = self.search_element_by_text('svg', self.TREE_DOTS_BUTTON_CSS)
        button.click()
        duplicate = self.search_element_by_text('li', self.DUPLICATE_CATALOG_TEXT)
        duplicate.click()

    def delete_catalog(self):
        button = self.search_element_by_text('svg', self.TREE_DOTS_BUTTON_CSS)
        button.click()
        duplicate = self.search_element_by_text('li', self.DELETE_CATALOG_TEXT)
        duplicate.click()

    def add_products_to_catalog(self):
        button = self.search_element_by_text('svg', self.TREE_DOTS_BUTTON_CSS)
        button.click()
        duplicate = self.search_element_by_text('li', self.ADD_ALL_PRODUCTS_OPTION_TEXT)
        duplicate.click()

    def edit_catalog(self):
        button = self.search_element_by_text('svg', self.TREE_DOTS_BUTTON_CSS)
        button.click()
        duplicate = self.search_element_by_text('li', self.EDIT_CATALOG_TEXT)
        duplicate.click()

    def create_order_from_catalog(self):
        span_tag = self.search_element_by_text('span', self.CREATE_ORDER_BUTTON_TEXT)
        button = span_tag.find_element_by_xpath('..')
        button.click()

    def download_price_list(self):
        span_tag = self.search_element_by_text('span', self.DOWNLOAD_PRICE_LIST_BUTTON_TEXT)
        button = span_tag.find_element_by_xpath('..')
        button.click()

    def download_clients_price_list(self):
        span_tag = self.search_element_by_text('span', self.DOWNLOAD_CLIENT_PRICE_LIST_TEXT)
        button = span_tag.find_element_by_xpath('..')
        button.click()

