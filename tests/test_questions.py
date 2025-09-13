import pytest
from pages.main_page import MainPage
from pages.questions_section import QuestionsSection
from selenium.webdriver.common.by import By
import allure

@pytest.mark.questions
class TestQuestions:
    @pytest.mark.parametrize('question',
                             ["question1", "question2", "question3", "question4", "question5", "question6", "question7",
                              "question8"])
    @allure.title("Проверка раскрытия вопроса {question}")
    def test_expand_each_question(self, driver, question):
        main_page = MainPage(driver)
        main_page.scroll_to_bottom()
        questions_section = QuestionsSection(driver)
        questions_section.expand_question(question)

        # Проверяем, открылось ли окно с вопросом
        expanded_block = questions_section.find_element((By.XPATH, f"//div[@id='accordion__panel-{question[-1]}']"))
        assert expanded_block.is_displayed(), f"Вопрос №{question} не раскрылся."