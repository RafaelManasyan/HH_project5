from project_folder.src.files_class_module import JSONSaver
from project_folder.src.vacancy_class import Vacancy
from src.api_class_module import HeadHunterAPI

hh_api = HeadHunterAPI()  # Создание экземпляра класса для работы с API сайтов с вакансиями
hh_vacancies = hh_api.get_vacancies("Python")  # Получение вакансий с hh.ru в формате JSON
vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)  # Преобразование набора данных из JSON в список объектов
# Пример работы конструктора класса с одной вакансией
vacancy = Vacancy("Python Developer",
                  "<https://hh.ru/vacancy/123456>",
                  "100 000",
                  "150 000 руб.",
                  "Требования: опыт работы от 3 лет...",
                  '000000000')

# Сохранение информации о вакансиях в файл
json_saver = JSONSaver()
json_saver.add_vacancy(vacancy)
json_saver.delete_vacancy(vacancy)


# Функция для взаимодействия с пользователем
def user_interaction():
    search_query = input("Введите поисковый запрос: ")
    vacancies_json_list = HeadHunterAPI().get_vacancies(search_query)

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print(top_vacancies)


if __name__ == "__main__":
    user_interaction()
