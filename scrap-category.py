import requests
import json
from bs4 import BeautifulSoup

print('hello world')
link = 'https://networkintegrators.ae'
Categories=[]
try:
    print("Extracting from "+link)
    response = requests.get(link)
    soup = BeautifulSoup(response.text,"html.parser")
    parents = soup.findAll('ul', attrs={'class':'category-list'})
    print(parents)
    # with open("maincategories.txt","w") as f:
        # f.write(parents)
    if parents != None:
        for parent in parents:
            # print(parent)


            a_elements = parent.select('div > ul > li.parent')
            
            # print(a_elements)
            # with open("categories.html","w") as f:
            #     f.write(a_elements)
            if a_elements:
                print('')
                for a in a_elements:
                    # print(a)  is ma saara parent class ka andar ka data ha 

                    getsubcategory1 = a.select('ul')
                    # if getsubcategory1 != None:
                        # for sub1 in getsubcategory1:




                    # text = a.text.strip()
                    # data_id = a.get('data-id') 
                    # Categories.append({'name':text})
                    # print(a_elements)
                    # with open("categories_ul.html","w") as f:
                    #     f.write(a.select('ul'))


                    # print("Anchor Text:", text)
                    # bc_elements = a.find('ul')
                    # print('------------------')
                    # print(parent.find('ul',attrs={'data-id':data_id }))
                    # print('------------------')
                    # Bc_elements = parent.select('ul > li.parent ',attrs={'data-id':data_id })
                    # print('------------------------------')
                    # print(Bc_elements.select('ul'))
                    # print('')
                    # print('------------------------------')
                    # print("Data ID Attribute:", data_id)
            else:
                print('No <a> elements whose parent is an <li> found in this <ul>')

            

            # GET ALL CATEGORIES
            # getparentctaegorys = parent.find_all('li', attrs={'class':'parent'})
            # if getparentctaegorys != None:
            #     for parentcatrgory in getparentctaegorys:
            #         for testcat in parentcatrgory.find('a',attrs={'data-id': True}):
            #             print(testcat)
            #         # print(parentcatrgory)
                    
            #     # print(getparentctaegorys)
            # else:
            #     print('nahi ha------------------------')

                
        # print(parents)
    else:
        print('No Data Found')        
except Exception as varname:
    print(varname)

# def fetchandsavefile()

# print(Categories)