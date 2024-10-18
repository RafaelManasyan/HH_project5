import psycopg2
from project_folder.src.DBCreate_module import DBConnection


class DBManager(DBConnection):
    """Класс для взаимодействия с базой данных"""

    def __init__(self):
        super().__init__()

    def get_companies_and_vacancies_count(self):
        """Метод для получения из базы данных названия компании и количества вакансий этой компании"""
        conn = psycopg2.connect(
            host=self._host,
            database=self._database,
            user=self._username,
            port=self._port,
            password=self._password,
        )
        cur = conn.cursor()
        cur.execute('''SELECT employers.company_name, COUNT(vacancies.employer_id)
        FROM employers JOIN vacancies USING (employer_id) GROUP BY employer_id''')
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result

    def get_all_vacancies(self):
        """Метод для получения информации по вакансии и названию компании"""
        conn = psycopg2.connect(
            host=self._host,
            database=self._database,
            user=self._username,
            port=self._port,
            password=self._password,
        )
        cur = conn.cursor()
        cur.execute('''SELECT employers.company_name, vacancies.vacancy_name, 
        ((vacancies.salary_from + vacancies.salary_to) / 2), vacancies.url
        FROM vacancies JOIN employers USING(employer_id)''')
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result

    def get_avg_salary(self):
        """Метод для получения средней зарплаты по вакансиям"""
        conn = psycopg2.connect(
            host=self._host,
            database=self._database,
            user=self._username,
            port=self._port,
            password=self._password,
        )
        cur = conn.cursor()
        cur.execute('''SELECT AVG((vacancies.salary_from + vacancies.salary_to) / 2) FROM vacancies''')
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result

    def get_vacancies_with_higher_salary(self):
        """Метод для получения вакансий с зарплатой выше среднего"""
        conn = psycopg2.connect(
            host=self._host,
            database=self._database,
            user=self._username,
            port=self._port,
            password=self._password,
        )
        cur = conn.cursor()
        cur.execute('''SELECT * FROM vacancies WHERE ((vacancies.salary_from + vacancies.salary_to) / 2) > 
(SELECT (AVG((vacancies.salary_from + vacancies.salary_to) / 2)) FROM vacancies)''')
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result

    def get_vacancies_with_keyword(self, keyword):
        """Метод для получения вакансий по ключевому слову"""
        conn = psycopg2.connect(
            host=self._host,
            database=self._database,
            user=self._username,
            port=self._port,
            password=self._password,
        )
        cur = conn.cursor()
        cur.execute(f"""SELECT * FROM vacancies 
        WHERE vacancy_name LIKE '%{keyword.title()}%' OR vacancy_name LIKE '%{keyword.lower()}%'""")
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result
