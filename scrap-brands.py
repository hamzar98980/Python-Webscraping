import requests
import json
from bs4 import BeautifulSoup

print('hello world')
link = 'https://networkintegrators.ae/networking.html'
Categories=[]
try:
    print("Extracting from "+link)
    response = requests.get(link)
    soup = BeautifulSoup(response.text,"html.parser")
    parents = soup.find('div', attrs={"data-bind":"scope: 'manufacturerFilter'"})
    # getlists = parents.findAll('div > ol')
    print(parents)


except Exception as varname:
    print(varname)

# def fetchandsavefile()

# print(Categories)