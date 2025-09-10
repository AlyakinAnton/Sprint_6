from .base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class QuestionsSection(BasePage):
    ACCORDION_HEADING_LOCATORS = {
        'question1': (By.XPATH, '//div[@id="accordion__heading-8"]'),
        'question2': (By.XPATH, '//div[@id="accordion__heading-9"]'),
        'question3': (By.XPATH, '//div[@id="accordion__heading-10"]'),
        'question4': (By.XPATH, '//div[@id="accordion__heading-11"]'),
        'question5': (By.XPATH, '//div[@id="accordion__heading-12"]'),
        'question6': (By.XPATH, '//div[@id="accordion__heading-13"]'),
        'question7': (By.XPATH, '//div[@id="accordion__heading-14"]'),
        'question8': (By.XPATH, '//div[@id="accordion__heading-15"]')
    }

    @allure.step("Расширить вопрос {question_id}")
    def expand_question(self, question_id):
        locator = self.ACCORDION_HEADING_LOCATORS.get(question_id)
        question_element = self.find_element(locator)
        self.scroll_into_view(question_element)
        self.move_to_element_and_click(question_element)