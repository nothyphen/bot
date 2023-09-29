#!/usr/bin/python

import requests, bs4

class ModelsWeather():

    def get_weather(city):
        query = city.replace('WEATHER', '').splitlines()[1]

        try:
            url = f"https://www.google.com/search?q=weather+{query.replace(' ', '')}"
            session = requests.session()
            session.headers['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
            page = session.get(url)
            soup = bs4.BeautifulSoup(page.text, 'html.parser')
            celsios = soup.find('span', attrs={'id':'wob_tm'}).text
            wind = soup.find('span', attrs={'id':'wob_ws'}).text
            humidity = soup.find('span', attrs={'id':'wob_hm'}).text
            time = soup.find('div', attrs={'id':'wob_dts'}).text
            weather = soup.find('div', attrs={'id':'wob_dcp'}).text
            data = {
                'ok' : 'ok',
                'celsion' : celsios,
                'wind' : wind,
                'humidity' : humidity,
                'time' : time,
                'weather' : weather,
            }
        except AttributeError:
            data ={
                'ok' : 'no'
            }

        return data