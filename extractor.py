from bs4 import BeautifulSoup
import urllib.request  as urllib2 
import requests
import re
from pymongo import MongoClient
import os


def extract_values(url,next_url):
    i=2
    arr_1 =[]
    arr_2 = []
    next_url = next_url + str(i)
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    arr_1 = extraction(soup,page)
    
    while True:
        i=i+1
        page_new = requests.get(next_url)
        if page_new.status_code != 200:
            break
        next_url = next_url + str(i)
        arr_2 = extraction(soup,page_new)
    merged_list = arr_1 + arr_2
    return merged_list
    


def extraction(soup,page):
    arr=[]
    values = soup.find_all('div', attrs={'class': 'btmMrg carlistblk'})
    for item in values:
        dict= {}
        URL = item.find(itemprop="image").get('content')
        title = item.find('div',attrs={'class':'carimgblk'}).img['title']
        year_manufacture = int(re.sub(u'[()]', '', re.search(u"[(]\d{4}[)]", title).group(0)))
        word_list = title.split()
        region = word_list[-1]
        price = item.find('div',attrs={'class':'cr_prc'}).text
        price = int(re.sub("[^\d\.]", "", price))
        if URL is None:
            URL = "Null"
        elif title is None:
            title = "Null"
        elif price is None:
            price ="Null"
        
        dict  = {"title":title,"URL":URL,"price":price,"currency":"Indian Rupee","region":region,"Man_year":year_manufacture}
        print(dict)
        arr.append (dict)
    return arr


def connect_to_mongo():
    try:
        client = MongoClient("mongodb://leexha:Password123_!@54.255.141.174/DATA_DB")
        print("Connection Successful")
    except:
        print("Connection Failure")
    return client

def insert_data(merged_list):
    try:
        conn = connect_to_mongo()
        mongo_db= conn.DATA_DB.collection
        result = mongo_db.insert_many(merged_list)
        print("insert successful")
    except :
        print("failed insert")


#execution of methods here
merged_list = extract_values("https://www.cartrade.com/buy-used-cars","https://www.cartrade.com/buy-used-cars/p-")
insert_data(merged_list)



