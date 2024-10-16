import psycopg2


class DBCreatingTable:
    """Класс для создания таблиц в базе данных PostgreSQL"""

    def __init__(self):
        self._host = "localhost"
        self._database = "postgres"
        self._username = "postgres"
        self._port = "5432"
        self._password = "nokwyz-2tigtY-pofjef"


class CreatingDBEmployersTable(DBCreatingTable):
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

    def db_filling_columns_for_emps(self, employers_list: list):
        try:
            conn = psycopg2.connect(
                host=self._host,
                database=self._database,
                user=self._username,
                port=self._port,
                password=self._password,
            )
            cur = conn.cursor()
            for employer in employers_list:
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


class CreatingDBVacanciesTable(DBCreatingTable):
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
