import requests
from bs4 import BeautifulSoup


# def aktau_parser():
#     r = requests.get('https://weather.rambler.ru/v-aktobe/3-days/')
#     html = BeautifulSoup(r.content, 'html.parser')
#
#     for temperature in html.find_all('div', attrs={'class': '_1S8F'}):
#         for temperature_2 in temperature('span', attrs={'class': '_3k_D'}):
#             temp = temperature_2.text
#             print(temp)
#
#     for precipitation in html.find_all('div', attrs={'class': '_1Y0B precipitationProbability'}):
#         for preccipitation_2 in precipitation.find_all('span', attrs={'class': '_1DZh'}):
#             prec = preccipitation_2.text
#             print(prec)
#
#     for wind_1 in html.find_all('div', attrs={'class': '_1Y0B wind'}):
#         for wind_2 in wind_1.find_all('span', attrs={'class': '_1DZh'}):
#             wind = wind_2.text
#             print(wind)

def aktau_parser():
    r = requests.get('https://weather.rambler.ru/v-aktobe/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for temperature in html.find_all('LNX8'):
        print(temperature)


def another_parser():
    r = requests.get('https://www.meteonova.ru/week/35229-Aktobe.htm')
    html = BeautifulSoup(r.content, 'html.parser')
    for elements in html.find_all('td', attrs={'class': 'fon_2_0 weather_td'}):
        for element in elements('td', attrs={'class': 'temper'}):
            print(element.text)

    for test1 in html.find_all('tr'):
        for test2 in test1.select_one(':nth-child(5)'):
            print(test2)


aktau_parser()
