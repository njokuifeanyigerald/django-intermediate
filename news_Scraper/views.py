from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
requests.packages.urllib3.disable_warnings()



def scrape():

    session = requests.Session()
    session.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}

    url = "https://www.theonion.com/"
    content = session.get(url, verify=False).content

    soup = BeautifulSoup(content, 'html.parser')
    posts = soup.find_all('article', {"class":"js_post_item sc-1pw4fyi-7 dCsSCd"})
    
    for i in posts:
        link = i.find('h4',{"class": 'sc-1qoge05-0 eoIfRA'})
        # image_source = i.find('img', {'class': "js_lazy-image sc-1dm5z0l-0 bUrcfY"})['srcset']
    #    DIV sc-1sm5z01-1 JPDWLR
    #     A sc-1pw4fyi-4 kdMDgR js_link sc-1out364-0 fwjlmD
        print(link.text)
        # print(image_source)
        # data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
        
        

scrape()