import pytest
from pages.main_page import MainPage
from urls.urls import BASE_URL, YANDEX_URL
import allure

@pytest.mark.navigation
class TestNavigation:
    @allure.title("Клик по логотипу Scooter")
    def test_click_on_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_logo_scooter()
        actual_url = main_page.get_current_url()  # Теперь через метод get_current_url
        expected_url = BASE_URL
        assert actual_url == expected_url, f"URL после клика по логотипу Scooter не соответствует: {actual_url}, ожидается: {expected_url}"

    @allure.title("Клик по логотипу Yandex")
    def test_click_on_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_logo_yandex()
        new_window_handle = main_page.driver.window_handles[-1]
        main_page.driver.switch_to.window(new_window_handle)
        actual_url = main_page.get_current_url()  # Аналогично
        expected_url = YANDEX_URL
        assert actual_url == expected_url, f"URL после клика по логотипу Yandex не соответствует: {actual_url}, ожидается: {expected_url}"