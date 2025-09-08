from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class OrdersForm:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы полей формы заказа
    NAME_FIELD_LOCATOR = ".//input[@placeholder='* Имя']"
    SURNAME_FIELD_LOCATOR = ".//input[@placeholder='* Фамилия']"
    ADDRESS_FIELD_LOCATOR = ".//input[@placeholder='* Адрес: куда привезти заказ']"
    METRO_STATION_FIELD_LOCATOR = ".//input[@placeholder='* Станция метро']"
    PHONE_FIELD_LOCATOR = ".//input[@placeholder='* Телефон: на него позвонит курьер']"
    NEXT_BUTTON_LOCATOR = ".//button[.='Далее']"

    DATE_PICKER_LOCATOR = ".//input[@placeholder='* Когда привезти самокат']"
    RENTAL_PERIOD_LOCATOR = ".//div[@class='Dropdown-placeholder'][contains(text(), '* Срок аренды')]"
    COLOR_BLACK_CHECKBOX_LOCATOR = "#black"
    COMMENT_FIELD_LOCATOR = ".//textarea[@placeholder='Комментарий для курьера']"
    PLACE_ORDER_BUTTON_LOCATOR = ".//button[.='Заказать']"
    CONFIRM_ORDER_BUTTON_LOCATOR = ".//button[.='Да']"
    SUCCESS_MESSAGE_LOCATOR = ".//div[contains(@class, 'Order_Modal__YZ-d3')]//*[contains(text(), 'успешно создан')]"

    def fill_name_field(self, full_name):
        first_name = full_name.split()[0]  # Берём только имя
        name_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.NAME_FIELD_LOCATOR))
        )
        name_field.clear()
        name_field.send_keys(first_name)

    def fill_surname_field(self, full_name):
        last_name = full_name.split()[1]  # Берём только фамилию
        surname_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.SURNAME_FIELD_LOCATOR))
        )
        surname_field.clear()
        surname_field.send_keys(last_name)

    def fill_address_field(self, address):
        address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ADDRESS_FIELD_LOCATOR))
        )
        address_field.clear()
        address_field.send_keys(address)

    def select_metro_station(self, metro):
        metro_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.METRO_STATION_FIELD_LOCATOR))
        )
        metro_field.send_keys(metro)  # Вводим название станции
        time.sleep(1)  # Ждём, пока появится список подсказок
        suggestions = self.driver.find_elements(By.CSS_SELECTOR, ".suggestion-list > div")  # Получаем список подсказок
        if suggestions:
            suggestions[0].click()  # Выбираем первый элемент из списка
        else:
            print("Предложения станций не найдены!")

    def fill_phone_field(self, phone):
        phone_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.PHONE_FIELD_LOCATOR))
        )
        phone_field.clear()
        phone_field.send_keys(phone)

    def next_step(self):
        next_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.NEXT_BUTTON_LOCATOR))
        )
        self.driver.execute_script("arguments[0].click();", next_button)  # Используем JavaScript-клик

    def set_delivery_date(self, date):
        delivery_date_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.DATE_PICKER_LOCATOR))
        )
        delivery_date_field.clear()
        delivery_date_field.send_keys(date)

    def choose_rental_period(self, period):
        rental_period_dropdown = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.RENTAL_PERIOD_LOCATOR))
        )
        rental_period_dropdown.click()
        selected_option = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f".//div[text()='{period}']"))
        )
        selected_option.click()

    def check_black_color(self):
        black_checkbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, self.COLOR_BLACK_CHECKBOX_LOCATOR))
        )
        if not black_checkbox.is_selected():
            black_checkbox.click()

    def submit_order(self):
        place_order_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PLACE_ORDER_BUTTON_LOCATOR))
        )
        place_order_button.click()

    def confirm_order(self):
        confirm_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.CONFIRM_ORDER_BUTTON_LOCATOR))
        )
        confirm_button.click()

    def verify_success_message(self):
        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.SUCCESS_MESSAGE_LOCATOR))
        )
        return success_message.text.strip() == "Ваш заказ успешно создан!"