import pytest
from pages.main_page import MainPage

@pytest.mark.navigation
class TestNavigation:
    def test_click_on_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_logo_scooter()
        current_url = driver.current_url
        expected_url = "https://qa-scooter.praktikum-services.ru/"  # Основная страница Яндекс.Самокат
        assert current_url == expected_url, f"Ошибка перенаправления по логотипу 'Самокат'. Текущая ссылка: {current_url}"

    def test_click_on_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.click_logo_yandex()
        new_window_handle = driver.window_handles[-1]
        driver.switch_to.window(new_window_handle)
        current_url = driver.current_url
        expected_url = "https://dzen.ru/?yredirect=true"  # Переход на Яндекс Дзен
        assert current_url == expected_url, f"Ошибка перенаправления по логотипу 'Яндекс'. Текущая ссылка: {current_url}"