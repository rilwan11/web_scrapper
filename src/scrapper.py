import requests
from bs4 import BeautifulSoup

def web():
    #collect user input 
    url = input ("Enter url to scrap: ") 
    print(url) 
    
    #get the text of the user's input
    code = requests.get(url)
    plain = code.text
    
    #convert the user's input into html
    s = BeautifulSoup(plain, "html.parser")
    print(s)
    
    #loop through the page dom elements that we need 
    # for link in s.findAll('a', {'class':'s-access-detail-page'}):
    #     tet = link.get('title')
    #     print(tet)
    #     tet_2 = link.get('href')
    #     print(tet_2)

        
