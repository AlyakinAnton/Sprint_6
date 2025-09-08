import pytest
from pages.main_page import MainPage
from pages.questions_section import QuestionsSection

@pytest.mark.questions
class TestQuestions:
    @pytest.mark.parametrize('question', ['question1', 'question2', 'question3', 'question4', 'question5', 'question6', 'question7', 'question8'])
    def test_expand_each_question(self, driver, question):
        main_page = MainPage(driver)
        main_page.scroll_to_bottom()  # Прокручиваем страницу до конца, чтобы добраться до раздела вопросов
        questions_section = QuestionsSection(driver)
        questions_section.expand_question(question)  # Раскрываем вопрос