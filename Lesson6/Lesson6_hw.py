# 1) Создать консольную программу-парсер, с выводом прогноза погоды. Дать
# возможность пользователю получить прогноз погоды в его локации ( по
# умолчанию) и в выбраной локации, на определенную пользователем дату.
# Можно реализовать, как консольную программу, так и веб страницу.
# Используемые инструменты: requests, beatifulsoup, остальное по желанию.
# На выбор можно спарсить страницу, либо же использовать какой-либо API.

import requests, bs4
import datetime
from dateutil.relativedelta import relativedelta
import json
from urllib.request import urlopen

# url = 'http://ipinfo.io/json'
# response = urlopen(url)
# data = json.load(response)

# IP=data['ip']
# org=data['org']
# city = data['city']
# country=data['country']
# region=data['region']
#
# print('Your IP detail\n ')
# print(f'IP : {IP} \nRegion : {region} \nCountry : {country} \nCity : {city} \nOrg : {org}')



def full_request(city='киев', date=''):
    part_site = 'https://sinoptik.ua/'
    part_site2 = 'погода-' + city
    if date != None:
        s = requests.get(f'{part_site}{part_site2}/{date}')
    else:
        s = requests.get(part_site + part_site2)
    b = bs4.BeautifulSoup(s.text, "html.parser")
    p1 = b.select('.temperature .p1')
    pog1 = p1[0].getText()
    p2 = b.select('.temperature .p2')
    pog2 = p2[0].getText()
    p3 = b.select('.temperature .p3')
    pog3 = p3[0].getText()
    p4 = b.select('.temperature .p4')
    pog4 = p4[0].getText()
    p5 = b.select('.temperature .p5')
    pog5 = p5[0].getText()
    p6 = b.select('.temperature .p6')
    pog6 = p6[0].getText()
    p7 = b.select('.temperature .p7')
    pog7 = p7[0].getText()
    p8 = b.select('.temperature .p8')
    if date == str(datetime.datetime.now())[:10]:
        pog8 = p8[0].getText()
        p9 = b.select('.date')
        pog9 = p9[0].getText()
        p10 = b.select('.month')
        pog10 = p10[0].getText()
    else:
        pog8 = p8[0].getText()
        p9 = b.select('.infoDate')
        pog9 = p9[0].getText()
        p10 = b.select('.infoMonth')
        pog10 = p10[0].getText()
    p = b.select('.rSide .description')
    pogoda = p[0].getText()

    print(f'{pog9} {pog10} {pogoda[2].lower()}{pogoda[3:]}')
    print(f'Погода ночью: от {pog1} до {pog2}\n'
          f'Погода утром: от {pog3} до {pog4}\n'
          f'Погода днем: от {pog5} до {pog6}\n'
          f'Погода вечером: от {pog7} до {pog8}\n')

def short_reuest(city='киев', date=''):
    part_site = 'https://sinoptik.ua/'
    part_site2 = 'погода-' + city
    if date != None:
        s = requests.get(f'{part_site}{part_site2}/{date}')
    else:
        s = requests.get(part_site + part_site2)
    b = bs4.BeautifulSoup(s.text, "html.parser")
    p1 = b.select('.temperature .p1')
    pog1 = p1[0].getText()
    p2 = b.select('.temperature .p2')
    pog2 = p2[0].getText()
    p3 = b.select('.temperature .p3')
    pog3 = p3[0].getText()
    p4 = b.select('.temperature .p4')
    pog4 = p4[0].getText()
    p9 = b.select('.infoDate')
    pog9 = p9[0].getText()
    p10 = b.select('.infoMonth')
    pog10 = p10[0].getText()
    p = b.select('.rSide .description')
    pogoda = p[0].getText()

    print(f'{pog9} {pog10} {pogoda[2].lower()}{pogoda[3:]}')
    print(f'Погода ночью: {pog1}\n'
          f'Погода утром: {pog2}\n'
          f'Погода днем: {pog3}\n'
          f'Погода вечером: {pog4}\n')

def start_request():
    site = 'https://sinoptik.ua/'
    s = requests.get(site)
    b = bs4.BeautifulSoup(s.text, "html.parser")
    p1 = b.select('.temperature .p1')
    pog1 = p1[0].getText()
    p2 = b.select('.temperature .p2')
    pog2 = p2[0].getText()
    p3 = b.select('.temperature .p3')
    pog3 = p3[0].getText()
    p4 = b.select('.temperature .p4')
    pog4 = p4[0].getText()
    p5 = b.select('.temperature .p5')
    pog5 = p5[0].getText()
    p6 = b.select('.temperature .p6')
    pog6 = p6[0].getText()
    p7 = b.select('.temperature .p7')
    pog7 = p7[0].getText()
    p8 = b.select('.temperature .p8')
    pog8 = p8[0].getText()
    p9 = b.select('.date')
    pog9 = p9[0].getText()
    p10 = b.select('.month')
    pog10 = p10[0].getText()

    p = b.select('.rSide .description')
    pogoda = p[0].getText()

    print(f'{pog9} {pog10} {pogoda[2].lower()}{pogoda[3:]}')
    print(f'Погода ночью: от {pog1} до {pog2}\n'
          f'Погода утром: от {pog3} до {pog4}\n'
          f'Погода днем: от {pog5} до {pog6}\n'
          f'Погода вечером: от {pog7} до {pog8}\n')


EXIT_ANSWERS = 'Y/y/Д/д'

start_request()

run = True
while run:
    city = input('Введите город, в котром хотите узнать прогноз погоды в именительном падеже')
    run2 = False
    while run2 == False:
        day_num = int(input('Введите колличество дней прогноза (до 10)'))
        if day_num > 0 and day_num <= 10:
            run2 = True
        else:
            run2 = False
    dates = []
    for i in range(int(day_num)):
        date = datetime.datetime.now() + relativedelta(days=i)
        dates.append(str(date)[:10])
    count = 0
    try:
        for date in dates:
            if count < 2:
                full_request(city, date)
                count += 1
            else:
                short_reuest(city, date)
    except IndexError:
        print('Город не найден')
        run = True

    answer = input(f'Если хотите выйти, нажмите{EXIT_ANSWERS}')
    if answer in EXIT_ANSWERS:
        run = False
    else:
        run = True




