# pages/orders_form.py
from .base_page import BasePage
from selenium.webdriver.common.by import By
import allure

class OrdersForm(BasePage):
    NAME_FIELD_LOCATOR = (By.XPATH, ".//input[@placeholder='* Имя']")
    SURNAME_FIELD_LOCATOR = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD_LOCATOR = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_FIELD_LOCATOR = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    PHONE_FIELD_LOCATOR = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON_LOCATOR = (By.XPATH, ".//button[.='Далее']")

    DATE_PICKER_LOCATOR = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_LOCATOR = (By.XPATH, ".//div[@class='Dropdown-placeholder'][contains(text(), '* Срок аренды')]")
    COLOR_BLACK_CHECKBOX_LOCATOR = (By.ID, "#black")
    COMMENT_FIELD_LOCATOR = (By.XPATH, ".//textarea[@placeholder='Комментарий для курьера']")
    PLACE_ORDER_BUTTON_LOCATOR = (By.XPATH, ".//button[.='Заказать']")
    CONFIRM_ORDER_BUTTON_LOCATOR = (By.XPATH, ".//button[.='Да']")
    SUCCESS_MESSAGE_LOCATOR = (By.XPATH, ".//div[contains(@class, 'Order_Modal__YZ-d3')]//*[contains(text(), 'успешно создан')]")

    @allure.step("Заполнить поле имени")
    def fill_name_field(self, name):
        name_field = self.find_element(self.NAME_FIELD_LOCATOR)
        name_field.clear()
        name_field.send_keys(name)

    @allure.step("Заполнить поле фамилии")
    def fill_surname_field(self, surname):
        surname_field = self.find_element(self.SURNAME_FIELD_LOCATOR)
        surname_field.clear()
        surname_field.send_keys(surname)

    @allure.step("Заполнить поле адреса доставки")
    def fill_address_field(self, address):
        address_field = self.find_element(self.ADDRESS_FIELD_LOCATOR)
        address_field.clear()
        address_field.send_keys(address)

    @allure.step("Выбрать станцию метро")
    def select_metro_station(self, metro):
        metro_field = self.find_element(self.METRO_STATION_FIELD_LOCATOR)
        metro_field.send_keys(metro)
        suggestions = self.find_elements((By.CSS_SELECTOR, ".suggestion-list > div"))
        if suggestions:
            suggestions[0].click()
        else:
            print("Предложения станций не найдены!")

    @allure.step("Заполнить номер телефона")
    def fill_phone_field(self, phone):
        phone_field = self.find_element(self.PHONE_FIELD_LOCATOR)
        phone_field.clear()
        phone_field.send_keys(phone)

    @allure.step("Продолжить оформление заказа")
    def next_step(self):
        next_button = self.wait_until_clickable(self.NEXT_BUTTON_LOCATOR)
        self.move_to_element_and_click(next_button)

    @allure.step("Указать дату доставки")
    def set_delivery_date(self, date):
        delivery_date_field = self.find_element(self.DATE_PICKER_LOCATOR)
        delivery_date_field.clear()
        delivery_date_field.send_keys(date)

    @allure.step("Выбрать срок аренды")
    def choose_rental_period(self, period):
        rental_period_dropdown = self.find_element(self.RENTAL_PERIOD_LOCATOR)
        rental_period_dropdown.click()
        selected_option = self.find_element((By.XPATH, f".//div[text()='{period}']"))
        selected_option.click()

    @allure.step("Выбрать черный цвет самоката")
    def check_black_color(self):
        black_checkbox = self.find_element(self.COLOR_BLACK_CHECKBOX_LOCATOR)
        if not black_checkbox.is_selected():
            black_checkbox.click()

    @allure.step("Подтвердить заказ")
    def submit_order(self):
        place_order_button = self.find_element(self.PLACE_ORDER_BUTTON_LOCATOR)
        self.move_to_element_and_click(place_order_button)

    @allure.step("Окончательно подтвердить заказ")
    def confirm_order(self):
        confirm_button = self.find_element(self.CONFIRM_ORDER_BUTTON_LOCATOR)
        self.move_to_element_and_click(confirm_button)

    @allure.step("Проверить успех заказа")
    def verify_success_message(self):
        success_message = self.find_element(self.SUCCESS_MESSAGE_LOCATOR)
        return success_message.text.strip() == "Ваш заказ успешно создан!"