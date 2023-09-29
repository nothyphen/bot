#!/usr/bin/python

import time
import requests
import urllib3

class Models():
    
    def __init__(self):
        self.url = "https://tracking.post.ir/search.aspx?id="

    def give_info(code):
        cookies = {
            'ASP.NET_SessionId': 'w4gbcayzsgrbewaxvhcfo51f',
            'BIGipServerPool_Farm_126': '2120548618.20480.0000',
        }
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'ASP.NET_SessionId=w4gbcayzsgrbewaxvhcfo51f; BIGipServerPool_Farm_126=2120548618.20480.0000',
            'Origin': 'https://tracking.post.ir',
            'Referer': 'https://tracking.post.ir/search.aspx?id=210160213903875520098147',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'X-MicrosoftAjax': 'Delta=true',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'id': code,
        }

        data = 'scripmanager1=pnlMain%7CbtnSearch&__LASTFOCUS=&__EVENTTARGET=btnSearch&__EVENTARGUMENT=&__VIEWSTATE=%2FeWlmYF%2FJHaTbwAGsO4i8vusltWBzgFKaL0%2BXyXXYW%2FDn%2FhQiWz7Q42NIN%2B7J23iySHU3M7IXNeNGhURMlTMKBPhxIC8OkJB1gzurK9BFFSdDNaL0%2FA%2BBhSJOJJ1iNSUi76aRs4sicENhMqCEtTjMW53BWpdu8yDFsGcwbyZgAcmcAYcQCSC0%2FYN1r4%2BSTrYqh1iW4Gf3kfbBaNMu8nwgG3tvwo32dCWr7eRZkVQkr%2FM8rzX9joymALj918UCkR%2Bp7jDbAbtWaRyWhPDb6YiSWupmYIk5u3LxCRC5D7GIdrVLVv5sPlheD6tzTlx9SszcB8HK%2FAQuPuHdrzw8DJ76F95esvPJlddMy3GFJSCrvx3wPNcfJ7H7R1U82nCRWaO9E0G1IAGq87gTfTeENHJh1M1TH3rUt1UM0qcKODqJeE2HDsTFqf6C4kGZQkZ%2BSe%2BOfaK5Mla1laOVIuVwkfIo4IVUMwOoFHypHAdtALu9o5qS0ZPVJZxOEy3LVIp99%2FlrolgVkKuectO4kE7UYXSk4qA5hA6X1M6GbFZD4Q%2F9cAlOH5y06QpYiQTK6eGo9IPHJxnWs2kR4ruQgKlr8DtpAFxXc9%2BNaFCzg7ScySFf9V7SAwgCe85o11xCo%2Fi6Hx1&__VIEWSTATEGENERATOR=BBBC20B8&__VIEWSTATEENCRYPTED=&__EVENTVALIDATION=DNgklPSI%2FEQf%2BD1sEp0OMaX9vKgUUtQFxEgwriTCKh2BG5eggdSTosh6H9ZEHtoSPT7Hw9mvksYC07huIIO00BDMnE5Xz90Yg4D%2BOEJfy%2B4%2Bcrqlt8HXyEt3KGut1hf8G3sgIGkIyamybtld0wJgYPfUgpqf9U7ntrt9p53v5iWLaFohwdxm3EM9S1%2Ff5mpO6TxtsMBDNZnKM%2BsbNgg9Zw%3D%3D&txtbSearch=210160213903875520098147&txtVoteReason=&txtVoteTel=&__ASYNCPOST=true&'

        res = requests.post('https://tracking.post.ir/', params=params, cookies=cookies, headers=headers, data=data, verify=False)

        return res.text