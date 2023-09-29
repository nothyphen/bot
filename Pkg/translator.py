#!/usr/bin/python

import requests, bs4

class Translate():
    def TranslaFarsi(words):
       words = words.replace("MEAN", "").splitlines()[1]

       url = f"https://vajehyab.com/?q={words.replace(' ', '+')}"
       session = requests.session()
       session.headers['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
       page = session.get(url)
       soup = bs4.BeautifulSoup(page.text, 'html.parser')
       try:
           mean = soup.find("p", attrs={'class':'--uwan2z'}).text
        
       except AttributeError:
           url = f"https://vajehyab.com/name/{words.replace(' ', '+')}?q={words.replace(' ', '+')}"
           session = requests.session()
           session.headers['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
           page = session.get(url)
           soup = bs4.BeautifulSoup(page.text, 'html.parser')
           mean = soup.find("div", attrs={"class":"--16ge55g"}).text
       result = f""

       for char in mean:
           if char in ('۱', '۲', '۳', '۴', '۵'):
               result += "\n" + char
           else :
               result += char
           
       return(result)