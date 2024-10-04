import pytest

from project_folder.src.vacancy_class import Vacancy


@pytest.fixture
def get_vac_object_class():
    return Vacancy("Python Developer",
                   "<https://hh.ru/vacancy/123456>",
                   "100 000",
                   "150 000",
                   "Требования: опыт работы от 3 лет...",
                   "000000000")


@pytest.fixture
def get_vac_object_list():
    return [{'id': '107449290', 'premium': False, 'name': 'Стажёр по направлению "Нагрузочное тестирование"',
          'department': {'id': '3529-3529-stat', 'name': 'Сбер. Начало карьеры'},
          'has_test': False,
          'response_letter_required': False, 'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
          'salary': {'from': None, 'to': 71800, 'currency': 'RUR', 'gross': True}, 'type': {'id': 'open',
                                                                                            'name': 'Открытая'},
          'address': None, 'response_url': None, 'sort_point_distance': None, 'published_at':
              '2024-09-18T12:55:01+0300', 'created_at': '2024-09-18T12:55:01+0300', 'archived': False,
          'apply_alternate_url':
              'https://hh.ru/applicant/vacancy_response?vacancyId=107449290', 'show_logo_in_search': None,
          'insider_interview':
              None, 'url': 'https://api.hh.ru/vacancies/107449290?host=hh.ru', 'alternate_url':
              'https://hh.ru/vacancy/107449290', 'relations': [], 'employer': {'id': '3529', 'name': 'СБЕР',
                                                                               'url': 'https://api.hh.ru/employers/3529',
                                                                               'alternate_url': 'https://hh.ru/employer/3529',
                                                                               'logo_urls': {'90':
                                                                                                 'https://img.hhcdn.ru/employer-logo/6865266.jpeg',
                                                                                             'original':
                                                                                                 'https://img.hhcdn.ru/employer-logo-original/1311252.jpg',
                                                                                             '240':
                                                                                                 'https://img.hhcdn.ru/employer-logo/6865267.jpeg'},
                                                                               'vacancies_url':
                                                                                   'https://api.hh.ru/vacancies?employer_id=3529',
                                                                               'accredited_it_employer': False,
                                                                               'trusted': True}, 'snippet': {
                'requirement': 'Необходимые навыки: — Ansible. — Apache Kafka. — OpenShift. — REST API. — понимание микросервиснойархитектуры.',
                'responsibility': 'Помоги повысить эффективность интеграции систем безопасности Сбера для быстрой реакции на любые инциденты. В рамках стажировки тебе предстоит: — изучать характеристики...'},
          'contacts': None, 'schedule': {'id': 'flexible', 'name': 'Гибкий график'}, 'working_days': [],
          'working_time_intervals': [],
          'working_time_modes': [], 'accept_temporary': False,
          'professional_roles': [{'id': '124', 'name': 'Тестировщик'}],
          'accept_incomplete_resumes': False, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
          'employment': {'id': 'probation', 'name': 'Стажировка'}, 'adv_response_url': None, 'is_adv_vacancy': False,
          'adv_context': None},
         {'id': '108089297', 'premium': False, 'name': 'Стажер-разработчик', 'department': None, 'has_test': False,
          'response_letter_required': False, 'area': {'id': '2', 'name': 'Санкт-Петербург',
                                                      'url': 'https://api.hh.ru/areas/2'},
          'salary': {'from': 50000, 'to': None, 'currency': 'RUR', 'gross': False},
          'type': {'id': 'open', 'name': 'Открытая'},
          'address': {'city': 'Санкт-Петербург', 'street': 'проспект Обуховской Обороны', 'building': '120К',
                      'lat': 59.866355, 'lng': 30.471349, 'description': None,
                      'raw': 'Санкт-Петербург, проспект Обуховской Обороны, 120К',
                      'metro': {'station_name': 'Пролетарская', 'line_name':
                          'Невско-Василеостровская', 'station_id': '16.234', 'line_id': '16', 'lat': 59.865,
                                'lng': 30.47}, 'metro_stations':
                          [{'station_name': 'Пролетарская', 'line_name': 'Невско-Василеостровская',
                            'station_id': '16.234', 'line_id': '16',
                            'lat': 59.865, 'lng': 30.47}], 'id': '3670113'}, 'response_url': None,
          'sort_point_distance': None, 'published_at':
              '2024-10-02T17:14:18+0300', 'created_at': '2024-10-02T17:14:18+0300', 'archived': False,
          'apply_alternate_url':
              'https://hh.ru/applicant/vacancy_response?vacancyId=108089297', 'show_logo_in_search': None,
          'insider_interview':
              None, 'url': 'https://api.hh.ru/vacancies/108089297?host=hh.ru', 'alternate_url':
              'https://hh.ru/vacancy/108089297', 'relations': [], 'employer': {'id': '577614', 'name': 'Строй-Отделка',
                                                                               'url': 'https://api.hh.ru/employers/577614',
                                                                               'alternate_url': 'https://hh.ru/employer/577614',
                                                                               'logo_urls': {
                                                                                   'original': 'https://img.hhcdn.ru/employer-logo-original/801432.jpg',
                                                                                   '90': 'https://img.hhcdn.ru/employer-logo/3646615.jpeg',
                                                                                   '240': 'https://img.hhcdn.ru/employer-logo/3646616.jpeg'},
                                                                               'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=577614',
                                                                               'accredited_it_employer': False,
                                                                               'trusted':
                                                                                   True}, 'snippet': {
             'requirement': '<highlighttext>Python</highlighttext> от 3.7. FastApi/Flask. Postgresql, Sqlalchemy. Docker, git. Selenium: HTML/CSS/React преимущество. Библиотеки для разработки телеграм-ботов. ',
             'responsibility': 'Развивать применение ИИ для автоматизации и оптимизации рабочих процессов внутри компании.'},
          'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
          'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
          'professional_roles': [{'id':
                                      '96', 'name': 'Программист, разработчик'}], 'accept_incomplete_resumes': False,
          'experience': {'id':
                             'noExperience', 'name': 'Нет опыта'},
          'employment': {'id': 'probation', 'name': 'Стажировка'}, 'adv_response_url':
              None, 'is_adv_vacancy': False, 'adv_context': None},
         {'id': '108001774', 'premium': False, 'name': 'Junior Python разработчик', 'department': None,
          'has_test': False, 'response_letter_required': True, 'area': {'id': '1',
                                                                        'name': 'Москва',
                                                                        'url': 'https://api.hh.ru/areas/1'},
          'salary': {'from': 125000, 'to': None, 'currency': 'RUR',
                     'gross': False}, 'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None,
          'sort_point_distance': None, 'published_at': '2024-10-01T14:57:35+0300',
          'created_at': '2024-10-01T14:57:35+0300',
          'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=108001774',
          'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/108001774?host=hh.ru', 'alternate_url':
              'https://hh.ru/vacancy/108001774', 'relations': [], 'employer': {'id': '11075572', 'name': 'Monogramm',
                                                                               'url': 'https://api.hh.ru/employers/11075572',
                                                                               'alternate_url': 'https://hh.ru/employer/11075572',
                                                                               'logo_urls':
                                                                                   None,
                                                                               'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=11075572',
                                                                               'accredited_it_employer': False,
                                                                               'trusted': True},
          'snippet': {'requirement': 'Базовые знания <highlighttext>Python</highlighttext>. Понимание ООП. '
                                     'Опыт работы с фреймворками (например, Django, Flask). Знание SQL. '
                                     'Базовые знания HTML, CSS, JavaScript. ',
                      'responsibility': 'Разработка и поддержка backend части приложения на <highlighttext>Python</highlighttext>. Работа с '
                                        'базами данных (например, PostgreSQL, MongoDB). Написание чистого, эффективного и хорошо...'},
          'contacts': None,
          'schedule': {'id': 'flexible', 'name': 'Гибкий график'}, 'working_days': [], 'working_time_intervals': [],
          'working_time_modes': [], 'accept_temporary': False,
          'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}], 'accept_incomplete_resumes': False,
          'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
          'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False,
          'adv_context': None}]
