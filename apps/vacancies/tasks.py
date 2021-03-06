# coding: utf-8
import urllib
from celery import shared_task
from apps.vacancies.parsers import VacancySync, YandexRabotaParser


@shared_task(ignore_result=True)
def update_vacancies():
    fulltime = {
        'rid': 213,
        'currency': 'RUR',
        'text': 'python программист',
        'strict': 'false',
        'employment': 'FULL_EMPLOYMENT'
    }
    part_time = fulltime.copy()
    part_time['employment'] = 'TEMPORARY_EMPLOYMENT'

    syncer = VacancySync(parsers=[
        YandexRabotaParser(urllib.parse.urlencode(fulltime), type='fulltime'),
        # Contract feed is broken as of 13 july (shows same data as fulltime)
        # YandexRabotaParser(urllib.parse.urlencode(part_time), type='contract')
    ])
    return syncer.sync()
