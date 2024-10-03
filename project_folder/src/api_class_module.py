import requests
from abc import ABC, abstractmethod


class ApiHH(ABC):

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HeadHunterAPI(ApiHH):
    """
    Класс для получения данных по вакансиям из API HeadHunter
    """

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []

    def __get_vacancies(self, keyword):
        self.__params['text'] = keyword
        while self.__params.get('page') != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()['items']
            self.__vacancies.extend(vacancies)
            self.__params['page'] += 1

    def get_vacancies(self, keyword):
        """
        Получаем список вакансий в формате json из одноименного приватного метода
        """
        self.__get_vacancies(keyword)
        return self.__vacancies
