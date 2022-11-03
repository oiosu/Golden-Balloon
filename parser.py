import json
import pprint
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
from articles.models import Product

def prase_product_title():
    driver = webdriver.Chrome()
    driver.get('https://www.myrealtrip.com/themes/1091/offers')
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    container = soup.select("h3 > div.CardTitle-module__title--WAHI8")

    for i in container:    
        title = i.text
        # pprint.pprint(title)
        
    return title

if __name__=='__main__':
    product_title = prase_product_title()
    for i in range(len(product_title)):
        Product(title=i).save()