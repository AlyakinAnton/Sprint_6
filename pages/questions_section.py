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

    EXPANDED_BLOCK_LOCATORS = {
        'question1': (By.XPATH, "//div[@id='accordion__panel-8']"),
        'question2': (By.XPATH, "//div[@id='accordion__panel-9']"),
        'question3': (By.XPATH, "//div[@id='accordion__panel-10']"),
        'question4': (By.XPATH, "//div[@id='accordion__panel-11']"),
        'question5': (By.XPATH, "//div[@id='accordion__panel-12']"),
        'question6': (By.XPATH, "//div[@id='accordion__panel-13']"),
        'question7': (By.XPATH, "//div[@id='accordion__panel-14']"),
        'question8': (By.XPATH, "//div[@id='accordion__panel-15']")
    }

    @allure.step("Расширить вопрос {question_id}")
    def expand_question(self, question_id):
        locator = self.ACCORDION_HEADING_LOCATORS.get(question_id)
        question_element = self.find_element(locator)
        self.scroll_into_view(question_element)
        self.move_to_element_and_click(question_element)

    @allure.step("Проверить, открыт ли вопрос {question_id}")
    def is_question_opened(self, question_id):
        locator = self.EXPANDED_BLOCK_LOCATORS.get(question_id)
        block = self.find_element(locator)
        return block.is_displayed()