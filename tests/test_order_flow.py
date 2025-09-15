import pytest
from pages.main_page import MainPage
from pages.orders_form import OrdersForm
from data.data import TEST_DATA
import allure

@pytest.mark.orderflow
class TestOrderFlow:
    @pytest.mark.parametrize('name,address,phone', TEST_DATA)
    @allure.title("Процесс заказа через верхнюю кнопку")
    def test_order_from_top_button(self, driver, name, address, phone):
        main_page = MainPage(driver)
        orders_form = OrdersForm(driver)

        main_page.open_top_order_button()

        orders_form.fill_name_field(name)
        orders_form.fill_surname_field(name)
        orders_form.fill_address_field(address)
        orders_form.select_metro_station("Черкизовская")
        orders_form.fill_phone_field(phone)
        orders_form.next_step()

        orders_form.set_delivery_date("07.09.2025")
        orders_form.choose_rental_period("Двое суток")
        orders_form.check_black_color()
        orders_form.submit_order()
        orders_form.confirm_order()

        assert orders_form.verify_success_message(), "Сообщение об успешном размещении заказа не найдено"

    @pytest.mark.parametrize('name,address,phone', TEST_DATA)
    @allure.title("Процесс заказа через нижнюю кнопку")
    def test_order_from_bottom_button(self, driver, name, address, phone):
        main_page = MainPage(driver)
        orders_form = OrdersForm(driver)

        main_page.scroll_to_bottom()
        main_page.open_bottom_order_button()

        orders_form.fill_name_field(name)
        orders_form.fill_surname_field(name)
        orders_form.fill_address_field(address)
        orders_form.select_metro_station("Черкизовская")
        orders_form.fill_phone_field(phone)
        orders_form.next_step()

        orders_form.set_delivery_date("07.09.2025")
        orders_form.choose_rental_period("Двое суток")
        orders_form.check_black_color()
        orders_form.submit_order()
        orders_form.confirm_order()

        assert orders_form.verify_success_message(), "Сообщение об успешном размещении заказа не найдено"