import pytest

from Tests.Pages.LoginPage import Login
from Tests.Pages.MenuPage import Menu
from Tests.Constants import Data as dt
from Tests.Constants import SearchText as st
from Tests.Constants import ExpectedResults as exp
from Tests.Pages.Suppliers.SuppliersPage import Suppliers
from Tests.Pages.Suppliers.SupplierDetailPage import SupplierDetails
from Tests.Pages.Suppliers.AddConfigurationPopup import AddConfiguration


class TestSuppliers:

    @pytest.mark.parametrize('supplier, supp_acc', dt.SUPPLIER_CASE_1)
    def test_suppliers_accounts(self, my_app, supplier, supp_acc):
        login_page = Login(my_app)
        menu_page = Menu(my_app)
        suppliers_page = Suppliers(my_app)
        supplier_details = SupplierDetails(my_app)

        # Login to portal
        login_page.login_to_portal(dt.EMAIL_USERNAME, dt.EMAIL_PASSWORD)
        # Go to Suppliers page
        menu_page.go_to_option(st.SUPPLIERS_TEXT)
        suppliers_page.go_to_supplier_by_name(supplier)
        assert supplier_details.check_accounts_are_present(supp_acc)


