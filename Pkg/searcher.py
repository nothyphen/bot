#!/usr/bin/python

import requests, bs4

class Models():

    def search(name):
        product = name.replace("search", "")
        line = product.splitlines()
        query = ""
        for i in range(len(line) - 1):
            query += str(line[i+1])
        
        session = requests.session()
        session.headers['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        page = session.get("https://torob.com/search/?query="+query+"&page=1")

        info = []
        product_names = []
        product_prices = []
        product_links = []

        soup = bs4.BeautifulSoup(page.text, 'lxml')
        names = soup.findAll('h2', attrs={'class':'product-name'})
        for name in names:
            product_names.append(str(name).replace('<h2 class="jsx-2514672dc9197d80 product-name">', '').replace("</h2>", ""))
        prices = soup.findAll('div', attrs={'class':'product-price-text'})
        for price in prices:
            product_prices.append(str(price).replace('<div class="jsx-2514672dc9197d80 product-price-text">از', '').replace("</div>", "").replace('<div class="jsx-2514672dc9197d80 product-price-text">', ''))
        
        for link in soup.find_all('div', attrs={'class':'jsx-2514672dc9197d80'}):
            a = link.find('a')
            if a != None:
                l = a['href']
                product_links.append("https://torob.com"+l)
        counter = 0
        for i in range(len(product_names)):
            if counter <= 4:
                info.append(product_names[i])
                info.append(product_prices[i])
                info.append(product_links[i]) 
                counter += 1
        return info
            