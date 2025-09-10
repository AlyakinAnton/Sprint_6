import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from allure_commons.types import AttachmentType
import allure


# Фикстура для управления драйвером (общая для всех тестов)
@pytest.fixture(scope="session")
def driver(request):
    """
    Инициализирует драйвер и закрывает его после окончания всех тестов.
    """
    chrome_options = Options()
    firefox_options = FirefoxOptions()

    # Параметры хром-драйвера
    chrome_options.add_argument('--headless')  # Безглавый режим (не показывает GUI)
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Параметры фаерфокс-драйвера
    firefox_options.add_argument('-headless')

    # Выбор драйвера
    driver = None
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == "firefox":
        driver = webdriver.Firefox(options=firefox_options)
    else:
        raise ValueError(f"Unsupported browser type: {browser}")

    # Максимизация окна (если не headless)
    if not '--headless' in str(chrome_options.arguments):
        driver.maximize_window()

    # Завершение работы драйвера после всех тестов
    request.addfinalizer(lambda: driver.quit())

    return driver


# Возможность передать аргумент типа браузера через командную строку
def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Choose browser: chrome/firefox")


# Аллюзии для детализации отчетов
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук для формирования детальных отчетов в Allure, включая логи и скриншоты.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        mode = "a" if rep.caplog else "w"
        try:
            log_file = item.session._setupstate._nailed_logfiles.get(item.nodeid)[0][0].split("/")[-1]
        except IndexError:
            log_file = ""

        if log_file:
            with open(log_file, mode) as f:
                content = f.read()
            context = "\n".join(
                [rep.longrepr.reprcrash.message, content]) if content else rep.longrepr.reprcrash.message
        else:
            context = rep.longrepr.reprcrash.message

        if hasattr(driver, "_web_driver"):
            driver_instance = getattr(driver, "_web_driver")
            screenshot = driver_instance.get_screenshot_as_png()
            allure.attach(screenshot, name="Screenshot", attachment_type=AttachmentType.PNG)
            allure.attach(context, name="Log", attachment_type=AttachmentType.TEXT)