from Tests.BaseWrapper.Driver import DriverWrapper


class OrderHistory(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ORDER_HISTORY_TABLE_CSS = ''
    GENERATE_REPORT_BUTTON_TEXT = 'Generate Report'
    BRAND_DROPDOWN_CSS = 'input[placeholder="All Brands"]'
    SEARCH_FIELD_NAME = 'searchText'
    SUPPLIER_DROPDOWN_CSS = 'input[placeholder="All Suppliers"]'
    CLIENT_DROPDOWN_CSS = 'input[placeholder="All Clients"]'
    CURRENCIES_DROPDOWN_CSS = 'input[placeholder="All Regions"]'
    REGIONS_DROPDOWN_CSS = 'input[placeholder="All Regions"]'
    STATUSES_DROPDOWN_CSS = 'input[placeholder="All Statuses"]'
    ORDER_TYPES_DROPDOWN_CSS = 'input[]'
    DATE_FROM_DATE_PICKER_NAME = 'dateFrom'
    DATE_TO_DATE_PICKER_NAME = 'dateTo'
    DENOMINATION_INPUT_NAME = 'faceValue'
    IS_DOWNLOADED_DROPDOWN_CSS = 'input[placeholder="All Orders"]'
    SEARCH_BUTTON_TEXT = 'Search'
    GO_TO_PREVIOUS_PAGE_CSS = ''
    GO_TO_NEXT_PAGE_CSS = ''
    GO_TO_PAGE_BY_NUM = ''
    ORDERS_PER_PAGE_CSS = ''
    ORDER_ROW_BY_ID = ''
    FIRST_ORDER_IN_LIST = ''
    ORDER_STATUS_COLUMN = ''
    CLIENT_COLUMN = ''
    LAST_ORDER_CLIENT = '//tr[1]/td[4]'

    def click_generate_report(self):
        button = self.search_element_by_text('span', self.GENERATE_REPORT_BUTTON_TEXT)
        button.find_element_by_xpath('..').click()

    def click_search_button(self):
        button = self.search_element_by_text('span', self.SEARCH_BUTTON_TEXT)
        button.find_element_by_xpath('..').click()

    def filter_by_search_field(self, text):
        self.input_in_search_field_name(self.SEARCH_FIELD_NAME, text)

    def filter_by_client(self, text):
        self.dropdown_input_css(self.CLIENT_DROPDOWN_CSS, text)

    def filter_by_brand(self, text):
        self.dropdown_input_css(self.BRAND_DROPDOWN_CSS, text)

    def filter_by_supplier(self, text):
        self.dropdown_input_css(self.SUPPLIER_DROPDOWN_CSS, text)

    def filter_by_currency(self, text):
        self.dropdown_input_css(self.CURRENCIES_DROPDOWN_CSS, text)

    def filter_by_status(self, text):
        self.dropdown_input_css(self.STATUSES_DROPDOWN_CSS, text)

    def filter_by_regions(self, text):
        self.dropdown_input_css(self.REGIONS_DROPDOWN_CSS, text)

    def filter_by_order_type(self, text):
        self.dropdown_input_css(self.ORDER_TYPES_DROPDOWN_CSS, text)

    def filter_by_denomination(self, text):
        self.input_in_search_field_name(self.DENOMINATION_INPUT_NAME, text)

    def filter_by_is_downloaded(self, text):
        self.dropdown_input_css(self.IS_DOWNLOADED_DROPDOWN_CSS, text)

    def filter_by_date_from(self, date):
        self.input_in_search_field_name(self.DATE_FROM_DATE_PICKER_NAME, date)

    def filter_by_date_to(self, date):
        self.input_in_search_field_name(self.DATE_TO_DATE_PICKER_NAME, date)

    def filter_by_region(self, text):
        self.dropdown_input_css(self.REGIONS_DROPDOWN_CSS, text)

    def filter_orders(self, supplier='', currency='', region='', client='', status='', order_type='', brand='',
                      is_downloaded='', denomination='', date_from='', date_to=''):
        if supplier != '':
            self.filter_by_supplier(supplier)
        if currency != '':
            self.filter_by_currency(currency)
        if region != '':
            self.filter_by_region(region)
        if client != '':
            self.filter_by_client(client)
        if status != '':
            self.filter_by_status(status)
        if order_type != '':
            self.filter_by_order_type(order_type)
        if brand != '':
            self.filter_by_brand(brand)
        if is_downloaded != '':
            self.filter_by_is_downloaded(is_downloaded)
        if denomination != '':
            self.filter_by_denomination(denomination)
        if date_from != '':
            self.filter_by_date_from(date_from)
        if date_to != '':
            self.filter_by_date_to(date_to)
        self.click_search_button()

    def search_order_by_text(self, text):
        self.input_in_search_field_name(self.SEARCH_FIELD_NAME, text)
        self.click_search_button()

    def check_last_order(self, client):
        act_client = self.search_element_by_css(self.LAST_ORDER_CLIENT)
        if act_client.text == client:
            return True
        else:
            return False

