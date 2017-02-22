#-*- coding: utf-8 -*-
# Created by JHJ on 2017. 2. 15.

import requests
import json


def get_news(query, id, secret):
    # Request
    # GET https://openapi.naver.com/v1/search/news.json

    try:
        response = requests.get(
            url="https://openapi.naver.com/v1/search/news.json",
            params={
                "query": query,
                "display": "10",
                "sort": "date",
            },
            headers={
                "X-Naver-Client-Id": id,
                "X-Naver-Client-Secret": secret,
            },
        )
        return json.loads(response.content.decode('utf-8'))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
        return False
