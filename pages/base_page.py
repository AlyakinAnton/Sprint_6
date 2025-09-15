# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from allure_commons.types import AttachmentType
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def move_to_element_and_click(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def wait_until_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def attach_screenshot(self, name):
        screenshot_bytes = self.driver.get_screenshot_as_png()
        allure.attach(screenshot_bytes, name=name, attachment_type=AttachmentType.PNG)

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_newest_window(self):
        handles = self.driver.window_handles
        newest_handle = handles[-1]
        self.driver.switch_to.window(newest_handle)