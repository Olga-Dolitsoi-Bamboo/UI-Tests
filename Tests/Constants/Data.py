from Tests.Constants import SearchText as st
from Tests.Constants import ExpectedResults as exp

"""Login"""
EMAIL_USERNAME = 'olga@bamboo-card.com'
EMAIL_PASSWORD = 'Odol2706####'
NEW_PASSWORD = 'Odol2706'

""" Menu tests """

CASE_1 = [(st.ORDERS_TEXT[0], st.ORDER_HISTORY_TEXT, st.ORDER_HISTORY_URL),
          (st.ORDERS_TEXT[0], st.SOPPING_CARTS_TEXT, st.SOPPING_CARTS_URL)
          ]
z = [(st.ORDERS_TEXT[0], st.CARDS_HISTORY_TEXT, st.CARDS_HISTORY_URL),
     (st.PRODUCTS_TEXT[0], st.PRODUCT_LIST_TEXT, st.PRODUCT_LIST_URL),
     (st.PRODUCTS_TEXT[0], st.CATALOGS_TEXT, st.CATALOGS_URL),
     (st.PRODUCTS_TEXT[0], st.PRODUCT_RULES_TEXT, st.PRODUCT_RULES_URL),
     (st.PRODUCTS_TEXT[0], st.INVENTORY_TEXT, st.INVENTORY_URL),
     (st.FINANCE_TEXT[0], st.INVOICES_TEXT, st.INVOICES_URL),
     (st.FINANCE_TEXT[0], st.FUNDING_TEXT, st.FUNDING_URL),
     (st.FINANCE_TEXT[0], st.RECONCILIATION_TEXT, st.RECONCILIATION_URL),
     (st.FINANCE_TEXT[0], st.TRANSACTIONS_TEXT, st.TRANSACTIONS_URL),
     (st.MARKETPLACES_TEXT[0], st.ENEBA_TEXT, st.ENEBA_URL),
     (st.MARKETPLACES_TEXT[0], st.GAMIVO_TEXT, st.GAMIVO_URL),
     (st.REPORTS_TEXT[0], st.BRANDS_REPORT_TEXT, st.BRANDS_REPORT_URL)]

""" Clients """
CLIENT_NAME_1 = 'Olga UI autotests1'
EXCHANGE_RATE_1 = '0'
INTEGRATION_TYPE_1 = 'Client'
COMMERCIAL_STRUCTURE_1 = 'Rebate'
SETTLEMENT_METHOD_1 = 'Cash'
ACCOUNT_TYPE_1 = 'Prepaid'
INVOICE_FREQUENCY_1 = 'Weekly'

CLIENT_NAME_2 = 'Olga UI autotests2'
EXCHANGE_RATE_2 = '2'
INTEGRATION_TYPE_2 = 'Manual'
COMMERCIAL_STRUCTURE_2 = 'Discounts'
SETTLEMENT_METHOD_2 = 'Cheque'
ACCOUNT_TYPE_2 = 'Postpaid'
INVOICE_FREQUENCY_2 = 'Monthly'
EXCHANGE_RATE_2_EDIT = '1'
SETTLEMENT_METHOD_2_EDIT = 'BankTransfer'

CLIENT_NAME_3 = '1'
EXCHANGE_RATE_3 = '-1'
COMMERCIAL_STRUCTURE_3 = 'Rebate'
ACCOUNT_TYPE_3 = 'Postpaid'
SETTLEMENT_METHOD_3 = 'Paypal'

CLIENT_NAME_4 = 'Olga UI autotests4'
EXCHANGE_RATE_4 = '5'
INTEGRATION_TYPE_4 = 'Client'
COMMERCIAL_STRUCTURE_4 = 'Discounts'
ACCOUNT_TYPE_4 = 'Postpaid'
SETTLEMENT_METHOD_4 = 'Paypal'
INVOICE_FREQUENCY_4 = 'Daily'
ACCOUNT_CURRENCY_4 = 'EUR'

"""Client error messages"""
NAME_ERROR_MESSAGE = 'The name must not be shorter than 2 characters.'
INTEGRATION_ERROR_MESSAGE = 'Type is required.'

"""Brands"""
BRAND_NAME_1 = 'Olga UI test brand'
BRAND_CURRENCY_1 = 'AED'
BRAND_REGION_1 = 'United Arab Emirates'
BRAND_DESCRIPTION_1 = 'This is my test brand'

"""Suppliers"""
SUPPLIER_NAME_CADOOZ = 'Cadooz'
SUPPLIER_NAME_CY_SEND = 'CY.SEND'
SUPPLIER_NAME_DIGGECARD = 'Diggecard'
SUPPLIER_NAME_EZPIN = 'Ezpin'
SUPPLIER_NAME_99_CIT = 'CIT99'
SUPPLIER_NAME_EPAY_MIDDLE_EAST = 'Epay Middle East'
SUPPLIER_NAME_JOKER_CODES_USD = 'Joker Codes (USD)'
SUPPLIER_NAME_JOKER_CODES_AED = 'Joker Codes (AED)'
SUPPLIER_NAME_PREPAID_FORGE = 'Prepaid Forge'
SUPPLIER_NAME_INCOMM = 'Incomm'
SUPPLIER_NAME_NI_SUPPLIER = 'Non integrated suppliers'
SUPPLIER_NAME_XOXO = 'XoXoDays (EUR)'

SUPPLIER_CASE_1 = [
    (SUPPLIER_NAME_INCOMM, exp.EXPECTED_ACCOUNTS_INCOMM)]

my = [(SUPPLIER_NAME_CY_SEND, exp.EXPECTED_ACCOUNTS_CY_SEND),
      (SUPPLIER_NAME_DIGGECARD, exp.EXPECTED_ACCOUNTS_DIGGECARD),
      (SUPPLIER_NAME_EZPIN, exp.EXPECTED_ACCOUNTS_EZPIN),
      (SUPPLIER_NAME_EPAY_MIDDLE_EAST, exp.EXPECTED_ACCOUNTS_EPAY_MIDDLE_EAST),
      (SUPPLIER_NAME_INCOMM, exp.EXPECTED_ACCOUNTS_INCOMM),
      (SUPPLIER_NAME_JOKER_CODES_AED, exp.EXPECTED_ACCOUNTS_JOKER_CODES_AED),
      (SUPPLIER_NAME_JOKER_CODES_USD, exp.EXPECTED_ACCOUNTS_JOKER_CODES_USD),
      (SUPPLIER_NAME_PREPAID_FORGE, exp.EXPECTED_ACCOUNTS_PREPAID_FORGE)]

"""CY.SEND PRODUCT CONFIGURATION"""
PRODUCT_CONFIG_ID_CASE_1 = '281888'
PRODUCT_CONFIG_COUNTRY_CASE_1 = 'United States of America'
PRODUCT_CONFIG_FACE_VALUE_CASE_1 = '5'
PRODUCT_CONFIG_PRODUCT_CURRENCY_CASE_1 = 'USD'
PRODUCT_CONFIG_SUPPLIER_PRICE_CASE_1 = '4.56'
PRODUCT_CONFIG_PRICE_CURRENCY_CASE_1 = 'EUR'
PRODUCT_CONFIG_VAT_VALUE_CASE_1 = '0'

PRODUCT_CONFIGURATION_CASE_1 = {'Product Code': PRODUCT_CONFIG_ID_CASE_1, 'Country': PRODUCT_CONFIG_COUNTRY_CASE_1,
                                'Face Value': PRODUCT_CONFIG_FACE_VALUE_CASE_1,
                                'Product Currency': PRODUCT_CONFIG_PRODUCT_CURRENCY_CASE_1,
                                'Supplier Price': PRODUCT_CONFIG_SUPPLIER_PRICE_CASE_1,
                                'Price Currency': PRODUCT_CONFIG_PRICE_CURRENCY_CASE_1,
                                'Vat Value': PRODUCT_CONFIG_VAT_VALUE_CASE_1}

"""Products"""
NI_PRODUCT_NAME_CASE_1 = 'UI test NI product 1'
NI_PRODUCT_DENOMINATION_CASE_1 = '10'
NI_PRODUCT_SKU_CASE_1 = 'UI-TEST-NI-PRODUCT-1-10-AED'
NI_PRODUCT_CURRENCY_CASE_1 = 'AED'
NI_PRODUCT_BRAND_CASE_1 = 'Do not change brand UI test'

"""Catalogs"""
CATALOG_NAME_CASE_1 = 'UI test Catalog 1'
CATALOG_DISCOUNT_CASE_1 = '1'
CATALOG_DESCRIPTION_CASE_1 = 'this is catalogs description'
CATALOG_TRANSACTION_FEE_CASE_1 = '2'
CATALOG_SUPPLIER_FEE_CASE_1 = '1'

CATALOG_IN_DB = 'UI test do not change'
CATALOGS_CLIENT_TO_ADD = 'UI test do not change'

"""Orders"""
CLIENT_FOR_ORDERS = 'UI test for order'
ACCOUNT_FOR_ORDERS = 'USD'
BRAND_FOR_ORDERS = 'Steam (EU/EUR)'
PRODUCT_FOR_ORDERS = 'Steam 10 EUR'
QUANTITY_FOR_ORDERS = '1'
