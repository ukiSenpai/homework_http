# Самый важный сайт для программистов это stackoverflow. И у него тоже есть API Нужно написать программу, которая
# выводит все вопросы за последние два дня и содержит тэг 'Python'. Для этого задания токен не требуется.
from datetime import datetime, timedelta
from pprint import pprint

import requests

ANALISYS_SYTE = 'stackoverflow'
API = 'https://api.stackexchange.com/'
POSTS_PREFIX = '/questions'
TAGS = ['Python']


def main():
    data = datetime.now() - timedelta(days=2)
    params = {
        'fromdate': int(data.timestamp()),
        'tagged': TAGS,
        'site': ANALISYS_SYTE
    }
    headers = {
        'Content-Type': 'application/json'
    }
    resp = requests.get(f"{API}{POSTS_PREFIX}", params=params, headers=headers)
    pprint(resp.json())


if __name__ == '__main__':
    main()
