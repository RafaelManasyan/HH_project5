import psycopg2


class DBConnection:
    """Класс для подключения к базе данных PostgreSQL"""

    def __init__(self):
        self._host = "localhost"
        self._database = "employers_vacancy"
        self._username = "postgres"
        self._port = "5432"
        self._password = "nokwyz-2tigtY-pofjef"


class DBCreating(DBConnection):
    """Класс для создания базы данных"""

    def __init__(self):
        super().__init__()
        self._database = "postgres"

    def create_db(self):
        conn = psycopg2.connect(
            host=self._host,
            database=self._database,
            user=self._username,
            port=self._port,
            password=self._password,
        )
        cur = conn.cursor()
        conn.autocommit = True
        cur.execute("""CREATE DATABASE employers_vacancy""")
        cur.close()
        conn.close()


class CreatingDBEmployersTable(DBConnection):
    """Класс для создания таблицы работодателей в базе данных PostgreSQL"""

    def __init__(self):
        super().__init__()

    def db_creating_employers(self) -> None:
        conn = psycopg2.connect(
            host=self._host,
            database=self._database,
            user=self._username,
            port=self._port,
            password=self._password,
        )
        cur = conn.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS employers 
            (employer_id varchar PRIMARY KEY,
            company_name varchar(50) UNIQUE,
            vacancies_count int)"""
        )
        conn.commit()
        cur.close()
        conn.close()

    def db_filling_columns_for_emps(self, employers_id_list: list, employers_list: list):
        filtered_employers_list = [emp for emp in employers_list if emp['id'] in employers_id_list]
        try:
            conn = psycopg2.connect(
                host=self._host,
                database=self._database,
                user=self._username,
                port=self._port,
                password=self._password,
            )
            cur = conn.cursor()
            for employer in filtered_employers_list:
                cur.execute(
                    """INSERT INTO employers (employer_id, company_name, vacancies_count) VALUES (%s, %s, %s)""",
                    (employer.get('id'), employer.get('name'), employer.get('open_vacancies'))
                )
            conn.commit()
        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            cur.close()
            conn.close()


class CreatingDBVacanciesTable(DBConnection):
    """Класс для создания таблицы вакансий в базе данных PostgreSQL"""
    def __init__(self):
        super().__init__()

    def db_creating_vacancies(self) -> None:
        conn = psycopg2.connect(
            host=self._host,
            database=self._database,
            user=self._username,
            port=self._port,
            password=self._password,
        )
        cur = conn.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS vacancies 
            (vacancy_id varchar PRIMARY KEY,
            vacancy_name varchar(50) NOT NULL,
            salary_from int,
            salary_to int,
            requirement text,
            url varchar NOT NULL,
            employer_id varchar,
            FOREIGN KEY (employer_id) REFERENCES employers (employer_id))"""
        )
        conn.commit()
        cur.close()
        conn.close()

    def db_filling_vacancies(self, vacancies_list: list):
        try:
            conn = psycopg2.connect(
                host=self._host,
                database=self._database,
                user=self._username,
                port=self._port,
                password=self._password,
            )
            cur = conn.cursor()
            for vacancy in vacancies_list:
                cur.execute(
                    """INSERT INTO vacancies 
                    (vacancy_id, vacancy_name, salary_from, salary_to, requirement, url, employer_id) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                    (
                        vacancy.get('id'),
                        vacancy.get('vacancy_name'),
                        vacancy.get('salary_from'),
                        vacancy.get('salary_to'),
                        vacancy.get('requirement'),
                        vacancy.get('vacancy_url'),
                        vacancy.get('employer_id')))
            conn.commit()
        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            cur.close()
            conn.close()


# x = CreatingDBEmployersTable().db_filling_columns_for_emps(list(1071925, 2180, 99759, 4352, 1740, 9173883, 26624, 15478, 62136, 3144945, 3959394), [{'id': '719302', 'name': 'Современные Технологии', 'url': 'https://api.hh.ru/employers/719302', 'alternate_url': 'https://hh.ru/employer/719302', 'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/147211.jpg', '240': 'https://img.hhcdn.ru/employer-logo/492638.jpeg', '90': 'https://img.hhcdn.ru/employer-logo/492637.jpeg'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=719302', 'open_vacancies': 0}, {'id': '720082', 'name': 'Инновации.Технологии.Производство', 'url': 'https://api.hh.ru/employers/720082', 'alternate_url': 'https://hh.ru/employer/720082', 'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/536619.jpg', '240': 'https://img.hhcdn.ru/employer-logo/2587950.jpeg', '90': 'https://img.hhcdn.ru/employer-logo/2587949.jpeg'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=720082', 'open_vacancies': 0}, {'id': '720298', 'name': 'Новые Строительные Технологии', 'url': 'https://api.hh.ru/employers/720298', 'alternate_url': 'https://hh.ru/employer/720298', 'logo_urls': None, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=720298', 'open_vacancies': 0}, {'id': '720353', 'name': 'Процессорные системы и технологии', 'url': 'https://api.hh.ru/employers/720353', 'alternate_url': 'https://hh.ru/employer/720353', 'logo_urls': None, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=720353', 'open_vacancies': 0}, {'id': '720484', 'name': 'Информационные Технологии Стабильности и Развития', 'url': 'https://api.hh.ru/employers/720484', 'alternate_url': 'https://hh.ru/employer/720484', 'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/147024.png', '240': 'https://img.hhcdn.ru/employer-logo/494456.png', '90': 'https://img.hhcdn.ru/employer-logo/494455.png'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=720484', 'open_vacancies': 0}, {'id': '721582', 'name': 'Университетский Центр Высоких Технологий', 'url': 'https://api.hh.ru/employers/721582', 'alternate_url': 'https://hh.ru/employer/721582', 'logo_urls': None, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=721582', 'open_vacancies': 0}, {'id': '722121', 'name': 'Технологии Тепла', 'url': 'https://api.hh.ru/employers/722121', 'alternate_url': 'https://hh.ru/employer/722121', 'logo_urls': None, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=722121', 'open_vacancies': 0}])
