from abc import ABC, abstractmethod

import requests


class ApiHH(ABC):

    @abstractmethod
    def __init__(self):
        pass


class FindVacancyFromHHApi(ApiHH):
    """
    Класс для получения данных по вакансиям из API HeadHunter
    """

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []

    def __get_vacancies(self, keyword: str):
        """Приватный метод получения списка ваканский"""
        self.__params["text"] = keyword
        try:
            while self.__params.get("page") != 20:
                if (
                    requests.get(
                        self.__url, headers=self.__headers, params=self.__params
                    ).status_code
                    == 200
                ):
                    response = requests.get(
                        self.__url, headers=self.__headers, params=self.__params
                    )
                    vacancies = response.json()["items"]
                    self.__vacancies.extend(vacancies)
                    self.__params["page"] += 1
        except Exception as e:
            print(f"Что-то не так с подключением, ошибка: {e}")

    def get_vacancies(self, keyword: str) -> list:
        """Получаем список вакансий в формате json из одноименного приватного метода"""
        self.__get_vacancies(keyword)
        return self.__vacancies


class FindEmployerFromHHApi(ApiHH):
    """
        Класс для получения данных по вакансиям из API HeadHunter
        """

    def __init__(self):
        self.__url = "https://api.hh.ru/employers"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100, "sort_by": "by_vacancies_open"}
        self.__employers = []

    def __get_employer_info(self, keyword=''):
        try:
            self.__params["text"] = keyword
            while self.__params.get("page") != 20:
                response = requests.get(
                    self.__url,
                    headers=self.__headers,
                    params=self.__params
            )
                employers = response.json()
                self.__employers.extend(employers["items"])
                self.__params["page"] += 1
        except Exception as e:
            print(f"Что-то не так с подключением, ошибка: {e}")

    def get_employer_info(self, keyword=''):
        self.__get_employer_info(keyword)
        return self.__employers
