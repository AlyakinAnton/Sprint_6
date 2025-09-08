from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class QuestionsSection:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы для вопросов
    ALL_QUESTIONS_LOCATORS = {
        'question1': '//div[@id="accordion__heading-8"]',
        'question2': '//div[@id="accordion__heading-9"]',
        'question3': '//div[@id="accordion__heading-10"]',
        'question4': '//div[@id="accordion__heading-11"]',
        'question5': '//div[@id="accordion__heading-12"]',
        'question6': '//div[@id="accordion__heading-13"]',
        'question7': '//div[@id="accordion__heading-14"]',
        'question8': '//div[@id="accordion__heading-15"]'
    }

    def expand_question(self, question_id):
        locator = self.ALL_QUESTIONS_LOCATORS.get(question_id)
        question_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, locator)),  # Ждём, пока элемент станет видимым
            message=f"Элемент '{locator}' не стал видимым в течение 20 секунд"
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", question_element)  # Прокручиваем элемент в центр экрана
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(question_element).perform()  # Наводим курсор на элемент
        action_chains.click(question_element).perform()  # Клик по элементу
        time.sleep(1)  # Немного ждём для полной уверенности