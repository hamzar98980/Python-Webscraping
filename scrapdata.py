import re
import requests
import json
from bs4 import BeautifulSoup

print('hello world')
link = 'https://networkintegrators.ae/networking.html'

def Scrapdatainhtml(url):
    print('fetching from ' + url)
    myresponse = requests.get(url)
    details_fetching = BeautifulSoup(myresponse.text,"html.parser")
    details = details_fetching.find('div', attrs={'class':'column main'})
    # print(details)
    # script_tag = soup.find('script', attrs={'type': 'text/x-magento-init'})
    # print(script_tag)
    return details

try:
    inutcategory=input('Enter Category Name: ')
    pagenumber = input('Enter Page Number: ')

    # category='networking'
    category=inutcategory
    jsondata={}
    counter = 1
    while counter <= int(pagenumber):

        print('Work start.............')
        link = f"https://networkintegrators.ae/{category}.html?p={counter}"
        print(link)
        response = requests.get(link)
      
        soup = BeautifulSoup(response.text,"html.parser")
        parents = soup.findAll('li', attrs={'class':'item product product-item'})
     
        counter=counter+1
        # print(parents)
        if parents != None and len(parents) != 0:
            print('data Exists')
            for parent in parents:
                prdiallitems = parent.find('div',attrs={'class':'product-item-info'})
                # print(prdiallitems)
                if prdiallitems != None:

                    prdname = prdiallitems.find('a',attrs={'class':'product-item-link'}).text.strip()
                    prdlink = prdiallitems.find('a',attrs={'class':'product-item-link'})['href']

                    print("Product Name: "+prdname)
                    print(prdlink)
                    
                    detailofproduct = Scrapdatainhtml(prdlink)
                    prdsku = detailofproduct.find('div',attrs={'class':'value', 'itemprop':'sku'}).text.strip()
                    prdincl_price = detailofproduct.select('div.product-info-price > div.price-final_price > span.price-container > span.price-including-tax > span.price')[0].text
                    prdext_price = detailofproduct.select('div.product-info-price > div.price-final_price > span.price-container > span.price-excluding-tax > span.price')[0].text
                    shortdecription = detailofproduct.find('div',attrs={"id":"short_description_content"}).text.strip()
                    longdescription = detailofproduct.select('div.product.attribute.description')[0].text
                    manufacturer = detailofproduct.find('td',attrs={"data-th":"Manufacturer"}).text.strip()
                    specifications = detailofproduct.find('td',attrs={"data-th":"Specification","class":"data"})
                    Eannumber = detailofproduct.find('td',attrs={"data-th":"EAN","class":"data"}).text.strip()

                    dataappend= {'name':prdname,'sku':prdsku,'prdlink':prdlink,'inclprice':prdincl_price,'exitprice':prdext_price,'shortdesc':shortdecription,'Ean':Eannumber,
                                     'longdescription':longdescription,
                                     'specifications':str(specifications),
                                     'brand':manufacturer}
                    
                    if category in jsondata:
                        jsondata[category].append(dataappend)
                    else:
                        jsondata[category] = [dataappend]

                    print("Sku: "+prdsku)
                    # print("Incl Price: "+prdincl_price)
                    # print("Ext Price: "+prdext_price)
                    # print("Brand: "+manufacturer)
                    # print("Eannumber: "+Eannumber)
                    # print(shortdecription)
                    # print(specifications)
                    # print(longdescription)

                    print("-------------")
        else:
            print('empty')
        # print(soup)
except Exception as varname:
    print(varname)

with open('products.json', 'w') as outfile:
    json.dump(jsondata, outfile)
# print(jsondata)

