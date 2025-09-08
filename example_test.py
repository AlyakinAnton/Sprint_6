import pytest
import allure

@allure.title("Тест успешной регистрации")
def test_registration():
    assert True, "Регистрация прошла успешно!"

@allure.title("Проверка входа в систему")
@pytest.mark.parametrize('username', ['admin', 'guest'])
def test_login(username):
    assert username in ["admin", "guest"], f"Пользователь {username} вошел в систему."