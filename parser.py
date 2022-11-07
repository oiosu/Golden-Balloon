import json
import pprint
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
from articles.models import Product
from urllib.request import urlopen

    
def prase_product():
    result = []
    driver = webdriver.Chrome()
    driver.get('https://www.myrealtrip.com/themes/1088/offers')
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    container = soup.select("h3 > div.CardTitle-module__title--WAHI8")
    detail_urls = soup.select("img.LazyImageLoader-module__image--FB3yN")

    title = []
    for i in container:    
        title.append(i.text ) 


    images = []
    
    for i in detail_urls:
        images.append(i["data-src"])
        
    driver.quit()
    
    file_no = 1
    for i in range(len(images)):
        with urlopen(images[i]) as f:
            with open('p_images/' + str(file_no)+'.jpeg', 'wb') as h:  
                img = f.read()
                h.write(img)
                file_no += 1    
    time.sleep(1)

    data = {}
    for i in range(len(title)):
        data[title[i]] = images[i]   
    return data 

    
if __name__=='__main__':
    product_data = prase_product()
    for i, j in product_data.items():
        Product(title = i, image = j).save()

    
# if __name__=='__main__':
#     product_title = prase_product_title()
#     for i in product_title:
#         Product(title=i).save()

        
# def prase_image():
#     driver = webdriver.Chrome()
#     driver.get('https://www.myrealtrip.com/themes/1088/offers')
#     html = driver.page_source
#     soup = BeautifulSoup(html, "html.parser")
    
#     detail_urls = soup.select("img.LazyImageLoader-module__image--FB3yN")

#     images = []
    
#     for i in detail_urls:
#         images.append(i["data-src"])
        
#     driver.quit()
    
#     file_no = 1
#     for i in range(len(images)):
#         with urlopen(images[i]) as f:
#             with open('./p_images' + str(file_no)+'.jpeg', 'wb') as h:  
#                 img = f.read()
#                 h.write(img)
#                 file_no += 1    
#     time.sleep(1)

#     return images

# if __name__=='__main__':
#     product_image = prase_image()
#     for j in product_image:
#         Product(image=j).save()
    