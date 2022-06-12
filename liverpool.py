#!/usr/bin/env python
# coding: utf-8


# installing the pakages:
    
# pip3 install pandas
# pip3 install 

# this code for Gathering information about Liver Pool's Players from the official web site.
# and collect it in the csv file.

import os
import pandas as pd
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from itertools import zip_longest

path = os.getcwd()

# initial lists: 
    
links = []
player_position = []
player_names = []
player_number = []
player_images = []


url = 'https://www.liverpoolfc.com/team/first-team'


client = urlopen(url)
html = client.read()
client.close()


soup = bs(html , 'html.parser')



containers = soup.find_all('div',{'class':'team-player-list'})


links = []
for container in containers:
    link = container.find_all('li',class_='team-player-list-item')
    for urls in link:
        links.append(urls.find('a').attrs['href'])
for i in range(len(links)):
    links[i] = url +'/'+ links[i][17:]



player_birthdate = []
player_place_birth = []
for link in links :
    client = urlopen(link)
    html = client.read()
    client.close()
    soup = bs(html , 'html.parser')
    containers2 = soup.find_all('div',{'class':'right'})
    for container2 in containers2:
        bdate = container2.find_all('div',class_ = 'dob')
        pbirth = container2.find_all('div',class_ = 'pob')
        player_birthdate.append(bdate[0].find('strong').text)
        player_place_birth.append(pbirth[0].find('strong').text)
#""""============"""


player_place_birth
len(player_place_birth)


for container in containers:
    pname = container.find_all('div',class_ = 'name')    
    ploc = container.find_all('h2',class_ = False)        
    pnum = container.find_all('div' , class_= 'number')
    pimg = container.find_all('div' , class_ = 'img-wrap')
    link = containers[0].find_all('li',class_='team-player-list-item')
    for i in range( len(pname)):
        player_names.append(pname[i].text)
        player_position.append(ploc[0].text)
        player_number.append(pnum[i].text)
        player_images.append(pimg[i].find('img').attrs['src'])
'=========================='


for i in range(len(player_names)):
    player_names[i] = re.sub('\n' , '',player_names[i])
    player_number[i] = int(player_number[i])


data = [player_number , player_names , player_position , player_birthdate , player_place_birth , player_images]
exported = zip_longest(*data)


# create DataFrame.

df = pd.DataFrame(exported , columns=['Player Number' , 'Player Name' , 'Player Position' ,'Player Bithday','place of Birth', 'Player Images'])

# save the data in csv file.

df.to_csv('liverpool.csv')

