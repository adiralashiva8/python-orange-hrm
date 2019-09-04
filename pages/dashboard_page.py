import test_data
from selenium import webdriver
from selenium.webdriver.common.by import By
from util.driver_util import DriverUtil


class Dashboard:

    def __init__(self, driver):
        self.driver = driver
        self.driver_util_obj = DriverUtil()

    _welcome_area = "//a[contains(text(), 'Welcome Admin')]"
    _pim_menu = "//a[normalize-space()='PIM']"
    _pim_add_employee_sub_menu = "//li[normalize-space()='Add Employee']"


    def dashboard_page_should_be_loaded(self):
        self.driver_util_obj.wait_for_element(self.driver, By.XPATH, self._welcome_area, test_data.element_timeout)
        assert "dashboard" in self.driver.current_url

    def go_to_add_employee_section(self):
        self.driver_util_obj.wait_for_element(self.driver, By.XPATH, self._pim_menu, test_data.element_timeout)
        self.driver.find_element_by_xpath(self._pim_menu)
        self.driver_util_obj.wait_for_element(self.driver, By.XPATH, self._pim_add_employee_sub_menu, test_data.element_timeout)
        self.driver.find_element_by_xpath(self._pim_add_employee_sub_menu)


