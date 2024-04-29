from tqdm import tqdm
import json
import re
import requests
from bs4 import BeautifulSoup

url = 'https://hh.ru/search/vacancy'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

params = {
    "area": [1, 2],  # Параметры для Санкт-Петербурга и Москвы
    "st": "searchVacancy",
    "text": "Python",
    "items_on_page": 20,  # Кол-во вакансии на странице, но максимальная глубина выдачи всех вакансий с 1991 по 2000 вакансий
}


def get_max_page():
    pages = []

    req = requests.get(url, headers=headers, params=params)
    print(req.url)

    soup = BeautifulSoup(req.text, "lxml")

    paginator = soup.find_all("span", {'class': 'pager-item-not-in-short-range'})
    for page in paginator:
        pages.append(int(page.find('a').text))

    return pages[-1]


def get_hh_jobs(last_page):
    jobs = []
    total_fields = 0

    for page in tqdm(range(last_page), desc='Processing pages'):
        count_page = {"page": page}
        params_page = {**params, **count_page}
        result = requests.get(url, headers=headers, params=params_page)
        soup = BeautifulSoup(result.text, "lxml")
        results = soup.find_all('div', {'class': 'vacancy-serp-item-body__main-info'})

        total_fields += len(results)

        for result in results:
            href = result.find('a', {'class': 'bloko-link'})['href']
            keywords_found = get_key_job(href)
            title_element = result.find('span', {'class': 'serp-item__title-link serp-item__title'})
            title = title_element.text if title_element else 'Not specified'

            address = result.find('div', {'data-qa': 'vacancy-serp__vacancy-address'})
            city = address.contents[0].strip() if address else 'Not specified'

            metro_station_span = address.find('span', {'class': 'metro-station'})
            metro_station = metro_station_span.text if metro_station_span else ''

            company_element = result.find('div', {'class': 'vacancy-serp-item__meta-info-company'})
            company = clean_text(company_element.find('span').text) if company_element and company_element.find('span') else 'Not specified'


            salary = result.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})
            salary_range = clean_text(salary.text) if salary else 'Нет вилки ЗП'

            if 'Django' in keywords_found and 'Flask' in keywords_found:
                job_info = {
                    'link': href,
                    'title': title,
                    'city': city,
                    'metro_station': metro_station,
                    'company': company,
                    'salary_range': salary_range,
                    'keywords': keywords_found
                }
                jobs.append(job_info)

    with open('hh_jobs.json', 'w', encoding='utf-8') as f:
        json.dump(jobs, f, ensure_ascii=False, indent=4)

    print(f"Общее количество вакансий на {last_page} страницах: {total_fields}")

    django_flask_jobs = [job for job in jobs if 'Django' in job['keywords'] and 'Flask' in job['keywords']]
    print(f"Количество вакансий с ключевыми словами Django и Flask: {len(django_flask_jobs)}")

    return jobs


def get_key_job(url_key):
    response = requests.get(url_key, headers=headers)
    found_keywords = []

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'lxml')

        keywords = [tag.text for tag in soup.find_all('span', {'class': 'bloko-tag__section bloko-tag__section_text'})]

        for keyword in keywords:
            if 'Django' in keyword or 'Flask' in keyword:
                found_keywords.append(keyword)

    return found_keywords


def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()
