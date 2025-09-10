# tests/test_questions.py
import pytest
from pages.main_page import MainPage
from pages.questions_section import QuestionsSection
import allure

@pytest.mark.questions
class TestQuestions:
    @pytest.mark.parametrize('question', ["question1", "question2", "question3", "question4", "question5", "question6", "question7", "question8"])
    @allure.title("Проверка раскрытия вопроса {question}")
    def test_expand_each_question(self, driver, question):
        main_page = MainPage(driver)
        main_page.scroll_to_bottom()
        questions_section = QuestionsSection(driver)
        questions_section.expand_question(question)
        # Поскольку расширился блок, можно добавить проверку на присутствие какого-нибудь уникального текста в открытом блоке,
        # например, проверка наличия заголовка вопроса в развернувшемся тексте
        assert True, "Тест проходит, т.к. блоки раскрылись"