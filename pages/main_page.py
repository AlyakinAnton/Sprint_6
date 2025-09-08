from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы
    LOGO_SCOOTER_LOCATOR = "(//img[@alt='Scooter'])[1]"  # Логотип Scooter
    LOGO_YANDEX_LOCATOR = "(//img[@alt='Yandex'])[1]"  # Логотип Yandex
    ORDER_BUTTON_TOP_LOCATOR = "//button[normalize-space()='Заказать']"  # Верхняя кнопка "Заказать"
    ORDER_BUTTON_BOTTOM_LOCATOR = "//button[contains(@class, 'Button_Button__ra12g') and normalize-space()='Заказать']"  # Нижняя кнопка "Заказать"

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def click_logo_scooter(self):
        scooter_logo = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LOGO_SCOOTER_LOCATOR)))
        scooter_logo.click()

    def click_logo_yandex(self):
        yandex_logo = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LOGO_YANDEX_LOCATOR)))
        yandex_logo.click()

    def open_top_order_button(self):
        top_order_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ORDER_BUTTON_TOP_LOCATOR)))
        top_order_btn.click()

    def open_bottom_order_button(self):
        bottom_order_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ORDER_BUTTON_BOTTOM_LOCATOR)))
        bottom_order_btn.click()