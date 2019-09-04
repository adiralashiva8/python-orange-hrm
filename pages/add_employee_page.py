import test_data
from selenium import webdriver
from selenium.webdriver.common.by import By
from util.driver_util import DriverUtil


class AddEmployee:

    def __init__(self, driver):
        self.driver = driver
        self.driver_util_obj = DriverUtil()
    
    _add_employee_text = "//a[contains(text(), 'Add Employee')]"

    def add_employee_page_should_be_loaded(self):
        self.driver_util_obj.wait_for_element(self.driver, By.XPATH, self._add_employee_text, test_data.element_timeout)
        assert "add_employee" in self.driver.current_url