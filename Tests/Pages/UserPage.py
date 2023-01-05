from Tests.BaseWrapper.Driver import DriverWrapper


class User(DriverWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""
