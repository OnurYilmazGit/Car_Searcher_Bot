import requests
from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import itertools
import schedule
import time
import random
from time import sleep
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'})

cars_url = 'https://www.autoscout24.de/lst/mercedes-benz/gle-(alle)?sort=price&desc=0&zip=&atype=C&ustate=N%2CU&powertype=kw&priceto=28000&ocs_listing=include&search_id=1mzom1wroxl'
r = get(cars_url, headers=headers)
page_html = BeautifulSoup(r.text, 'html.parser')

car_containers = page_html.find_all('article', class_="cldt-summary-full-item css-1dy5n47")

firstcar = car_containers[0]

firstcar.find_all('span')


print("Name Result " + firstcar.find_all('span')[0].text) 
firstspan=firstcar.find_all('span')[5].text
print('First result:' + firstspan) 
secondspan=firstcar.find_all('span')[6].text
print('Second result:' + secondspan) 
thirdspan=firstcar.find_all('span')[7].text
print('Third result:' + thirdspan)  


link_containers = page_html.find_all('div', class_="css-zjik7")

firstlink=link_containers[0]

for a in firstlink.find_all('a', href=True):
	link_car = a['href']
	print("Found the URL:", a['href'])

price=firstcar.find_all('span')[5].text
price = ''.join(filter(lambda i: i.isdigit(), price))

price = int(price)

limit = 65000

if price<limit:
	if car_containers != []:
		for container in car_containers:
			def crawlcar():
				schedule.every(30).seconds.do(crawcar)			

def telegram_bot_sendtext(bot_message):
    bot_token = '5154812445:AAGpPuWzbkxcGTCIv_wJDa8EtAKnRm7Ug5Y'
    bot_chatID = '1820102470'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()
message = telegram_bot_sendtext('A new car has been found!' +'\n'+ 'Price :' + str('€ '+str(price)) + '\n' + 'KM :' + firstcar.find_all('span')[6].text + '\n' + 'Model :' + firstcar.find_all('span')[7].text + '\n' +
 'Link: ' + 'www.autoscout24.de' + link_car)
