from Tests.BaseWrapper.Driver import DriverWrapper


class InactiveProducts(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


