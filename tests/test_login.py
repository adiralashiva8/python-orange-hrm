import pytest
import unittest
import test_data
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import Dashboard


class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(test_data.app_url)

    @pytest.mark.login
    def test_validate_login_to_orange_hrm_with_valid_credentials(self):
        login_page_obj = LoginPage(self.driver)
        login_page_obj.login_page_should_be_loaded()
        login_page_obj.input_user_name(test_data.user_name)
        login_page_obj.input_password(test_data.password)
        login_page_obj.click_login_button()
        dashboard_page_obj = Dashboard(self.driver)
        dashboard_page_obj.dashboard_page_should_be_loaded()

    @pytest.mark.regression
    @pytest.mark.login
    def test_validate_login_to_orange_hrm_with_invalid_credentials(self):
        login_page_obj = LoginPage(self.driver)
        login_page_obj.login_page_should_be_loaded()
        login_page_obj.input_user_name("Admin")
        login_page_obj.input_password("123")
        login_page_obj.click_login_button()
        login_page_obj.invalid_credentials_error_message_should_be_displayed

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.TestCase