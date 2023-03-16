from Tests import DriverWrapper



ORDER_HISTORY_URL = ''
ORDER_HISTORY_TABLE_CSS = ''
GENERATE_REPORT_BUTTON_CSS = ''
BRAND_DROPDOWN_ID = ''
SEARCH_FIELD_CSS = ''
SUPPLIER_DROPDOWN_ID = ''
CLIENT_DROPDOWN_ID = ''


class OrderHistoryPage(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver





