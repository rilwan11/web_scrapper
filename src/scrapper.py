import requests
from bs4 import BeautifulSoup
def web(page,WebUrl):
    if(page>0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        print(tet_2)
        # for link in s.findAll('a', {'class':'s-access-detail-page'}):
        #     tet = link.get('title')
        #     print(tet)
        #     tet_2 = link.get('href')
        #     print(tet_2)
