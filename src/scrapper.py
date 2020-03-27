import requests
from bs4 import BeautifulSoup
def web():
    url = input ("Enter url to scrap:") 
    print(url) 
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")
    print(s)
    # for link in s.findAll('a', {'class':'s-access-detail-page'}):
    #     tet = link.get('title')
    #     print(tet)
    #     tet_2 = link.get('href')
    #     print(tet_2)

        
