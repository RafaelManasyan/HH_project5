from project_folder.src.files_class_module import JSONSaver
from project_folder.src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies
from project_folder.src.vacancy_class import Vacancy
from src.api_class_module import HeadHunterAPI


# Пример работы конструктора класса с одной вакансией
vacancy = Vacancy("Python Developer",
                  "<https://hh.ru/vacancy/123456>",
                  "100 000",
                  "150 000",
                  "Требования: опыт работы от 3 лет...",
                  '000000000')

# Сохранение информации о вакансиях в файл
JSONSaver().add_vacancy(vacancy)
JSONSaver().delete_vacancy(vacancy)


# Функция для взаимодействия с пользователем
def user_interaction():
    search_query = input("Введите поисковый запрос: ")
    hh_vacancies = HeadHunterAPI().get_vacancies(search_query) # Получение вакансий с hh.ru в формате JSON
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)  # Преобразование набора данных из JSON в список объектов

    top_n = int(input("Введите количество вакансий для вывода N самых оплачиваемых: "))
    filter_words = list(input("Введите ключевые слова для фильтрации вакансий: ").split())
    salary_range_from = input("Введите диапазон зарплат от: ") # Пример: 100000
    salary_range_to = input("Введите диапазон зарплат до: ") # Пример: 150000
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range_from, salary_range_to)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print(filtered_vacancies)


if __name__ == "__main__":
    user_interaction()
