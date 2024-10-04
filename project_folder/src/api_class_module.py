from abc import ABC, abstractmethod

import requests


class ApiHH(ABC):

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HeadHunterAPI(ApiHH):
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
                if requests.get(
                    self.__url, headers=self.__headers, params=self.__params
                ).status_code == 200:
                    response = requests.get(
                        self.__url, headers=self.__headers, params=self.__params
                    )
                    vacancies = response.json()["items"]
                    self.__vacancies.extend(vacancies)
                    self.__params["page"] += 1
        except Exception as e:
            print(f"Что-то не так с подключением, ошибка: {e}")

    def get_vacancies(self, keyword: str) -> list:
        """ Получаем список вакансий в формате json из одноименного приватного метода"""
        self.__get_vacancies(keyword)
        return self.__vacancies
