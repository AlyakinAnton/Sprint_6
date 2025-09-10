from .base_page import BasePage
from selenium.webdriver.common.by import By
import allure

class MainPage(BasePage):
    LOGO_SCOOTER_LOCATOR = (By.XPATH, "(//img[@alt='Scooter'])[1]")
    LOGO_YANDEX_LOCATOR = (By.XPATH, "(//img[@alt='Yandex'])[1]")
    ORDER_BUTTON_TOP_LOCATOR = (By.XPATH, "//button[normalize-space()='Заказать']")
    ORDER_BUTTON_BOTTOM_LOCATOR = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and normalize-space()='Заказать']")

    @allure.step("Прокрутить страницу до низа")
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Кликнуть на логотип Scooter")
    def click_logo_scooter(self):
        logo = self.find_element(MainPage.LOGO_SCOOTER_LOCATOR)
        self.move_to_element_and_click(logo)

    @allure.step("Кликнуть на логотип Yandex")
    def click_logo_yandex(self):
        logo = self.find_element(MainPage.LOGO_YANDEX_LOCATOR)
        self.move_to_element_and_click(logo)

    @allure.step("Открыть верхний блок заказа")
    def open_top_order_button(self):
        btn = self.find_element(MainPage.ORDER_BUTTON_TOP_LOCATOR)
        self.move_to_element_and_click(btn)

    @allure.step("Открыть нижний блок заказа")
    def open_bottom_order_button(self):
        btn = self.find_element(MainPage.ORDER_BUTTON_BOTTOM_LOCATOR)
        self.move_to_element_and_click(btn)