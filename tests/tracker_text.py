import requests

cookies = {
    'ASP.NET_SessionId': '3f5avww40tjvlqhfpeirqoqr',
    'BIGipServerPool_Farm_126': '2120548618.20480.0000',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'ASP.NET_SessionId=3f5avww40tjvlqhfpeirqoqr; BIGipServerPool_Farm_126=2120548618.20480.0000',
    'Origin': 'https://tracking.post.ir',
    'Referer': 'https://tracking.post.ir/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
    'X-MicrosoftAjax': 'Delta=true',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = 'scripmanager1=pnlMain%7CbtnSearch&__LASTFOCUS=&__EVENTTARGET=btnSearch&__EVENTARGUMENT=&__VIEWSTATE=99OZQa9hADTz3axBtb1XNYOP3sZ6f1oyaogImOCpcbuArkPRD12rVg7s4rcJfdf2%2B1ionwBZX1W7wKjUhSp6V4bIsk9Q%2FQzEELNlokcf90S7vNJuRaHsHI7g9qN2OzFnwvxOlnBKhKo%2FI7KeCdOQKekJOTKCk2nnTzCbpEtppH9PSrw96SjPxHMGcmH0hYx7joqldDtJgo5P4eEd3JNNLFbZktermxm4flf1w%2F4SE75EP3Jg%2B7E7eZt5sfY4nTROUSSE2HgXlqAvf7q1aFz2R%2BgOnis6PTHOJX0nNds4i2VjO%2BvB68kPR0cT49u2W7mN3MZu04C5mIX7WGt7n8iMSuwwRVUtyR1iHlAnKUIVoMhJ3Rf3%2BjhIKpdGxkLPo6o2Cnn7eTSvsfqky06I%2BVMHcz0EiZSROOuGUcpd4G9XUL3sqY5qUM8bxbz0CST3enEKAViQWFCvTOXji%2FVFU81wogMJFPE11zsMujbi9OkiKEXuUiqIlRnU4fhUf3MWmMtFWhpgYPXWTYf2OOFD78i5BB3OpcrP%2FwAYaUrhQapUUS9XM%2FKyX2%2Bgtg83iG52J3ZM2EdbIB7hlpH6tJkQEJC3ELjnv4%2F4BEcyJnrW9uYam80CTAVT4rUGTyak0ODV1xaT&__VIEWSTATEGENERATOR=BBBC20B8&__VIEWSTATEENCRYPTED=&__EVENTVALIDATION=c2xgY34wUqP5QJd5NJlp1wB2x8XhRqe%2B4l%2BhONBAfO3VlvENo8RQThRCtomz2YUiZ4y0dYGVgjsAUkLBR5IQ9lYuu8G%2FE%2B2eaAtjxA5LCyOpGdYTD5ekhP6pFqGXvYvrDvBCGSfTyHhIEpmKyDLjVnGoi8NaV3ZwPDGJ0yOYT2TmTpi7Z6a7FAP3kFF%2ForLL80nuxn9A4Q8hNkhyPoqg5w%3D%3D&txtbSearch=210160213903875520098147&txtVoteReason=&txtVoteTel=&__ASYNCPOST=true&'

custom_certificate_path = "_.post.ir.crt"

response = requests.post('https://tracking.post.ir/', cookies=cookies, headers=headers, data=data, verify=custom_certificate_path)


cookies = {
    'ASP.NET_SessionId': '3f5avww40tjvlqhfpeirqoqr',
    'BIGipServerPool_Farm_126': '2120548618.20480.0000',
}

headers = {
    'Accept': 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'ASP.NET_SessionId=3f5avww40tjvlqhfpeirqoqr; BIGipServerPool_Farm_126=2120548618.20480.0000',
    'Referer': 'https://tracking.post.ir/',
    'Sec-Fetch-Dest': 'image',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'uid': '2007',
    'pid': '50124',
}

response = requests.get('https://tracking.post.ir/ShowImage.aspx', params=params, cookies=cookies, headers=headers, verify=custom_certificate_path)


cookies = {
    'ASP.NET_SessionId': '3f5avww40tjvlqhfpeirqoqr',
    'BIGipServerPool_Farm_126': '2120548618.20480.0000',
}

headers = {
    'Accept': 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'ASP.NET_SessionId=3f5avww40tjvlqhfpeirqoqr; BIGipServerPool_Farm_126=2120548618.20480.0000',
    'Referer': 'https://tracking.post.ir/',
    'Sec-Fetch-Dest': 'image',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://tracking.post.ir/Content/Image/postarmsitewhite.png', cookies=cookies, headers=headers, verify=custom_certificate_path)


cookies = {
    'ASP.NET_SessionId': '3f5avww40tjvlqhfpeirqoqr',
    'BIGipServerPool_Farm_126': '2120548618.20480.0000',
}

headers = {
    'Accept': 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'ASP.NET_SessionId=3f5avww40tjvlqhfpeirqoqr; BIGipServerPool_Farm_126=2120548618.20480.0000',
    'Referer': 'https://tracking.post.ir/',
    'Sec-Fetch-Dest': 'image',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://tracking.post.ir/Content/Image/rahgirigicon-white0.png', cookies=cookies, headers=headers, verify=custom_certificate_path)