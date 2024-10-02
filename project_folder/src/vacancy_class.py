from abc import ABC, abstractmethod


class VacancyABC(ABC):

    @abstractmethod
    def cast_to_object_list(self, json_vacancies):
        pass


class Vacancy(VacancyABC):
    __slots__ = ('__vacancy_name', '__vacancy_url', '__salary_from', '__salary_to', '__requirement', '__id')

    def __init__(self, vacancy_name, vacancy_url, salary_from, salary_to, requirement, vacancy_id):
        self.__vacancy_name: str = vacancy_name
        self.__vacancy_url: str = vacancy_url if vacancy_url else 'Ссылка не указана'
        self.__salary_from: int = salary_from if salary_to else 0
        self.__salary_to: int = salary_to if salary_to else 0
        self.__requirement: str = requirement if requirement else 'Требования не указаны'
        self.__id: str = vacancy_id

    @classmethod
    def cast_to_object_list(cls, json_vacancies):
        """
        Классовый метод для преобразования списка словарей(вакансий) в формате json, полученный от API HH.ru,
        в список объектов Vacancy
        """
        vacancies_list = []
        for vacancy in json_vacancies:
            vacancy_new = cls(vacancy.get('name'),
                              vacancy.get('alternate_url'),
                              vacancy.get('salary').get('from') if vacancy.get('salary') else None,
                              vacancy.get('salary').get('to') if vacancy.get('salary') else None,
                              vacancy.get('snippet').get('requirement'),
                              vacancy.get('id') if len(vacancy.get('id')) == 9 else 'Unknown')
            vacancies_list.append(vacancy_new)
        return vacancies_list

    @property
    def get_vacancy_info(self):
        vacancy_dict = {"name": self.__vacancy_name,
                        "url": self.__vacancy_url,
                        "salary_from": self.__salary_from,
                        "salary_to": self.__salary_from,
                        "requirement": self.__requirement,
                        "id": self.__id}
        return vacancy_dict
