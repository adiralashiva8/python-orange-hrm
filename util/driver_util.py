from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DriverUtil:

    def __init__(self):
        pass

    def wait_for_element(self, driver, locator_type, element, timeout):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((locator_type, element))
            )
        except:
            print("Couldn't find %s using %s in page after %s seconds"%(element, locator_type, str(timeout)))
            assert False
