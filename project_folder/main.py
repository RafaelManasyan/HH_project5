from project_folder.src.DBCreate_module import CreatingDBEmployersTable, DBCreating
from project_folder.src.api_class_module import FindVacancyFromHHApi, FindEmployerFromHHApi

from project_folder.src.utils import (
    filter_vacancies,
    get_top_vacancies,
    get_vacancies_by_salary,
    sort_vacancies,
)
from project_folder.src.vacancy_class import Vacancy


def user_interaction():
    """Функция для взаимодействия с пользователем"""
    search_query = input("Введите поисковый запрос: ")
    hh_vacancies = FindVacancyFromHHApi().get_vacancies(
        search_query
    )  # Получение вакансий с hh.ru в формате JSON
    vacancies_list = Vacancy.cast_to_object_list(
        hh_vacancies
    )  # Преобразование набора данных из JSON в список объектов
    top_n = int(input("Введите количество вакансий для вывода N самых оплачиваемых: "))
    filter_words = list(
        input("Введите ключевые слова для фильтрации вакансий: ").split()
    )
    salary_range_from = input("Введите диапазон зарплат от: ")  # Пример: 100000
    salary_range_to = input("Введите диапазон зарплат до: ")  # Пример: 150000
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = get_vacancies_by_salary(
        filtered_vacancies, salary_range_from, salary_range_to
    )
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print(top_vacancies)


def user_interaction_with_db():
    """Функция для создания, заполнения и взаимодействия пользователя с базой данных вакансий"""
    employer_word = input('Введите слово по которому хотите найти работодателя или оставьте поле пустым:\n')
    employers_count = int(input('Введите топ N (число до 50) ваканский для просмотра:\n'))
    employers = FindEmployerFromHHApi().get_employer_info(employers_count, keyword=employer_word)
    employers_id_list = list(input('Введите через запятую id не менее 10 компаний, за которыми хотите следить:\n').split(', '))
    DBCreating().create_db()
    CreatingDBEmployersTable().db_creating_employers()
    CreatingDBEmployersTable().db_filling_columns_for_emps(employers_id_list, employers)
    


if __name__ == "__main__":
    user_interaction_with_db()
# 1071925, 2180, 99759, 4352, 1740, 9173883, 26624, 15478, 62136, 3144945, 3959394