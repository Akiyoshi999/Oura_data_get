# -*- coding: utf-8 -*-
import imp
import requests
import calendar
import datetime
from urllib import parse
import configparser

def get_oura_data():
    '''
    OuraのAPIよりデータを取得する処理
    '''
    config_ini = configparser.ConfigParser()
    config_ini.read('config.ini', encoding='utf-8')

    urls = {
        'sleep' : 'https://api.ouraring.com/v1/sleep?',
        'active' : 'https://api.ouraring.com/v1/activity?',
        'readiness' : 'https://api.ouraring.com/v1/readiness?'
    }

    TOKEN = config_ini['OURA']['Token']

    trigger_week_day = config_ini['TARGET']['Trigger_week_day']
    current_date = datetime.date.today()
    get_week_day = calendar.day_name[current_date.weekday()]
    end_date = current_date - datetime.timedelta(days=1)

    if get_week_day == trigger_week_day:
        start_day = end_date - datetime.timedelta(weeks=1)
    else:
        start_day = end_date

    item_data = {
        'start': start_day.strftime('%Y-%m-%d'),
        'end' : end_date.strftime('%Y-%m-%d'),
        'access_token' : TOKEN,
    }

    sleep_score = []
    active_score = []
    readiness_score = []
    today_scores = {}
    week_scores = {}

    d_qs = parse.urlencode(item_data)
    for obj, url in urls.items():
        url = url + d_qs
        r_post = requests.get(url=url)
        r_post = r_post.json()
        for target in r_post.values():
            for tar in target:
                if obj == 'sleep':
                    sleep_score.append(tar['score'])
                elif obj == 'active':
                    active_score.append(tar['score'])
                elif obj == 'readiness':
                    readiness_score.append(tar['score'])

    # print('sleep_score: {}'.format(sleep_score))
    # print('active_score: {}'.format(active_score))
    # print('readiness_score: {}'.format(readiness_score))

    today_scores = {
        'sleep' : sleep_score[-1],
        'active' : active_score[-1],
        'readiness' : readiness_score[-1],
    }
    if len(sleep_score) > 1:
        week_scores = {
            'sleep' : round(sum(sleep_score) / len(sleep_score), 1),
            'active' : round(sum(active_score) / len(active_score), 1),
            'readiness' : round(sum(readiness_score) / len(readiness_score), 1),
        }
    return today_scores, week_scores
    
if __name__ == '__main__':
    get_oura_data()
