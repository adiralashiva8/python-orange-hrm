import pytest
import unittest
import test_data
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import Dashboard
import time


class Employee(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(test_data.app_url)

    @pytest.mark.employee
    def test_validate_create_employee(self):
        self.login_to_orange_hrm()
        dashboard_page_obj = Dashboard(self.driver)
        dashboard_page_obj.dashboard_page_should_be_loaded()
        dashboard_page_obj.go_to_add_employee_section()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()

    def login_to_orange_hrm(self):
        login_page_obj = LoginPage(self.driver)
        login_page_obj.login_page_should_be_loaded()
        login_page_obj.input_user_name(test_data.user_name)
        login_page_obj.input_password(test_data.password)
        login_page_obj.click_login_button()


if __name__ == "__main__":
    unittest.TestCase