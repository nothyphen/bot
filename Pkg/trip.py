#!/usr/bin/python

import requests

class Trip():
    def space(msg):
        msg = msg.replace("TRIP", "").splitlines()[1].split(" ")
        origin = msg[0]
        destination = msg[1]
        url = f"https://api.codebazan.ir/distance/index.php?mabda={origin}&maghsad={destination}"

        session = requests.session()
        session.headers['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        page = session.get(url)
        return page.text