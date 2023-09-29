#!/usr/bin/python

import requests, json

class Dollor():
    def check():
        url = "http://api.navasan.tech/latest/?api_key="+"freeMnIZkk9Kfyty8pJYhQSG0qdUs9ko"
        session = requests.session()
        session.headers['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        page = session.get(url)
        price = json.loads(page.text)
        return price['harat_naghdi_buy']['value']