import test_data
from selenium import webdriver
from selenium.webdriver.common.by import By
from util.driver_util import DriverUtil


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver_util_obj = DriverUtil()

    """
    Locators of log page
    """
    _user_name_text_box = "txtUsername"
    _password_text_box = "txtPassword"
    _login_button = "btnLogin"
    _invalid_credentials_message = "//span[text()='Invalid credentials']"

    """
    Keyword of login page
    """
    def login_page_should_be_loaded(self):
        self.driver_util_obj.wait_for_element(self.driver, By.ID, self._user_name_text_box, test_data.element_timeout)
        assert "login" in self.driver.current_url

    def input_user_name(self, user_name):
        self.driver_util_obj.wait_for_element(self.driver, By.ID, self._user_name_text_box, test_data.element_timeout)
        self.driver.find_element_by_id(self._user_name_text_box).send_keys(user_name)

    def input_password(self, password):
        self.driver_util_obj.wait_for_element(self.driver, By.ID, self._password_text_box, test_data.element_timeout)
        self.driver.find_element_by_id(self._password_text_box).send_keys(password)

    def click_login_button(self):
        self.driver_util_obj.wait_for_element(self.driver, By.ID, self._login_button, test_data.element_timeout)
        self.driver.find_element_by_id(self._login_button).click()

    def invalid_credentials_error_message_should_be_displayed(self):
        self.driver_util_obj\
            .wait_for_element(self.driver, By.XPATH, self._invalid_credentials_message, test_data.element_timeout)
