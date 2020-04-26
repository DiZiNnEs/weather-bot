import requests
from bs4 import BeautifulSoup


def aktau_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-aktau-mangistauskoy-oblasti/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(2)'):
        temp = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''
Прогнозы на завтра:
Температура: {temp}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
'''
        return result


def aktobe_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-aktobe/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(2)'):
        temp = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''
Прогнозы на завтра:
Температура: {temp}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
'''
        return result


def almaty_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-almaty/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(2)'):
        temp = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''
Прогнозы на завтра:
Температура: {temp}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
'''
        return result


def atyrau_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-atyrau/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(2)'):
        temp = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''
Прогнозы на завтра:
Температура: {temp}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
'''
        return result


def zhezkazgan_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-zhezkazgane-dzhezkazgane/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(2)'):
        temp = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''
Прогнозы на завтра:
Температура: {temp}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
'''
        return result


def karaganda_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-karagande/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(2)'):
        temp = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''
Прогнозы на завтра:
Температура: {temp}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
'''
        return result


def kyzylorda_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-kyzylorde/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(2)'):
        temp = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''
Прогнозы на завтра:
Температура: {temp}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
'''
        return result


def kokshetau_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-kokshetau/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(2)'):
        temp = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''
Прогнозы на завтра:
Температура: {temp}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
'''
        return result


def kostanai_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-kostanae/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(2)'):
        temp = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''
Прогнозы на завтра:
Температура: {temp}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
'''
        return result


def nursultan_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-nur-sultane/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(2)'):
        temp = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''
Прогнозы на завтра:
Температура: {temp}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
'''
        return result


def nursultan_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-nur-sultane/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(2)'):
        temp = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''
Прогнозы на завтра:
Температура: {temp}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
'''
        return result


def pavlodar_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-pavlodare/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(2)'):
        temp = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''
Прогнозы на завтра:
Температура: {temp}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
'''
        return result


def petropavlovsk_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-petropavlovske/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(2)'):
        temp = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''
Прогнозы на завтра:
Температура: {temp}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
'''
        return result


def semipalatinsk_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-semipalatinske/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(2)'):
        temp = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''
Прогнозы на завтра:
Температура: {temp}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
'''
        return result


def stepnogorsk_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-stepnogorske/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(2)'):
        temp = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''
Прогнозы на завтра:
Температура: {temp}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
'''
        return result


def taldykorgan_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-taldykorgane/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(2)'):
        temp = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''
Прогнозы на завтра:
Температура: {temp}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
'''
        return result


def temirtau_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-temirtau/kazakhstan/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(2)'):
        temp = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''
Прогнозы на завтра:
Температура: {temp}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
'''
        return result





