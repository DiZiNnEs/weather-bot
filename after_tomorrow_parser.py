import requests
from bs4 import BeautifulSoup


def aktau_after_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-aktau-mangistauskoy-oblasti/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(3)'):
        night_temperature = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for determine_temperature in tomorrow.select('div._3wdR:nth-child(2)'):
            day_temperature = determine_temperature.select_one('span._3k_D').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''\
Прогноз погоды на после завтра:
Температура ночью: {night_temperature}
Температура днём: {day_temperature}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
    '''
        return result


def aktobe_after_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-aktobe/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(3)'):
        night_temperature = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for determine_temperature in tomorrow.select('div._3wdR:nth-child(2)'):
            day_temperature = determine_temperature.select_one('span._3k_D').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''\
Прогноз погоды на после завтра:
Температура ночью: {night_temperature}
Температура днём: {day_temperature}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
        '''
        return result


def almaty_after_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-almaty/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(3)'):
        night_temperature = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for determine_temperature in tomorrow.select('div._3wdR:nth-child(2)'):
            day_temperature = determine_temperature.select_one('span._3k_D').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''\
Прогноз погоды на после завтра:
Температура ночью: {night_temperature}
Температура днём: {day_temperature}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
        '''
        return result


def atyrau_after_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-atyrau/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(3)'):
        night_temperature = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for determine_temperature in tomorrow.select('div._3wdR:nth-child(2)'):
            day_temperature = determine_temperature.select_one('span._3k_D').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''\
Прогноз погоды на после завтра:
Температура ночью: {night_temperature}
Температура днём: {day_temperature}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
        '''
        return result


def zhezkazgan_after_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-zhezkazgane-dzhezkazgane/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(3)'):
        night_temperature = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for determine_temperature in tomorrow.select('div._3wdR:nth-child(2)'):
            day_temperature = determine_temperature.select_one('span._3k_D').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''\
Прогноз погоды на после завтра:
Температура ночью: {night_temperature}
Температура днём: {day_temperature}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
        '''
        return result


def karaganda_after_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-karagande/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(3)'):
        night_temperature = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for determine_temperature in tomorrow.select('div._3wdR:nth-child(2)'):
            day_temperature = determine_temperature.select_one('span._3k_D').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''\
Прогноз погоды на после завтра:
Температура ночью: {night_temperature}
Температура днём: {day_temperature}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
        '''
        return result


def kyzylorda_after_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-kyzylorde/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(3)'):
        night_temperature = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for determine_temperature in tomorrow.select('div._3wdR:nth-child(2)'):
            day_temperature = determine_temperature.select_one('span._3k_D').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''\
Прогноз погоды на после завтра:
Температура ночью: {night_temperature}
Температура днём: {day_temperature}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
        '''
        return result


def kokshetau_after_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-kokshetau/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(3)'):
        night_temperature = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for determine_temperature in tomorrow.select('div._3wdR:nth-child(2)'):
            day_temperature = determine_temperature.select_one('span._3k_D').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''\
Прогноз погоды на после завтра:
Температура ночью: {night_temperature}
Температура днём: {day_temperature}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
        '''
        return result


def kostanai_after_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-kostanae/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(3)'):
        night_temperature = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for determine_temperature in tomorrow.select('div._3wdR:nth-child(2)'):
            day_temperature = determine_temperature.select_one('span._3k_D').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''\
Прогноз погоды на после завтра:
Температура ночью: {night_temperature}
Температура днём: {day_temperature}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
        '''
        return result


def nursultan_after_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-nur-sultane/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(3)'):
        night_temperature = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for determine_temperature in tomorrow.select('div._3wdR:nth-child(2)'):
            day_temperature = determine_temperature.select_one('span._3k_D').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''\
Прогноз погоды на после завтра:
Температура ночью: {night_temperature}
Температура днём: {day_temperature}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
        '''
        return result


def pavlodar_after_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-pavlodare/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(3)'):
        night_temperature = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for determine_temperature in tomorrow.select('div._3wdR:nth-child(2)'):
            day_temperature = determine_temperature.select_one('span._3k_D').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''\
Прогноз погоды на после завтра:
Температура ночью: {night_temperature}
Температура днём: {day_temperature}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
        '''
        return result


def petropavlovsk_after_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-petropavlovske/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(3)'):
        night_temperature = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for determine_temperature in tomorrow.select('div._3wdR:nth-child(2)'):
            day_temperature = determine_temperature.select_one('span._3k_D').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''\
Прогноз погоды на после завтра:
Температура ночью: {night_temperature}
Температура днём: {day_temperature}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
        '''
        return result


def semipalatinsk_after_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-semipalatinske/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(3)'):
        night_temperature = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for determine_temperature in tomorrow.select('div._3wdR:nth-child(2)'):
            day_temperature = determine_temperature.select_one('span._3k_D').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''\
Прогноз погоды на после завтра:
Температура ночью: {night_temperature}
Температура днём: {day_temperature}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
        '''
        return result


def stepnogorsk_after_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-stepnogorske/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(3)'):
        night_temperature = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for determine_temperature in tomorrow.select('div._3wdR:nth-child(2)'):
            day_temperature = determine_temperature.select_one('span._3k_D').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''\
Прогноз погоды на после завтра:
Температура ночью: {night_temperature}
Температура днём: {day_temperature}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
        '''
        return result


def taldykorgan_after_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-taldykorgane/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(3)'):
        night_temperature = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for determine_temperature in tomorrow.select('div._3wdR:nth-child(2)'):
            day_temperature = determine_temperature.select_one('span._3k_D').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''\
Прогноз погоды на после завтра:
Температура ночью: {night_temperature}
Температура днём: {day_temperature}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
        '''
        return result


def temirtau_after_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-temirtau/kazakhstan/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(3)'):
        night_temperature = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for determine_temperature in tomorrow.select('div._3wdR:nth-child(2)'):
            day_temperature = determine_temperature.select_one('span._3k_D').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''\
Прогноз погоды на после завтра:
Температура ночью: {night_temperature}
Температура днём: {day_temperature}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
        '''
        return result


def oskemen_after_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-ust-kamenogorske/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(3)'):
        night_temperature = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for determine_temperature in tomorrow.select('div._3wdR:nth-child(2)'):
            day_temperature = determine_temperature.select_one('span._3k_D').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''\
Прогноз погоды на после завтра:
Температура ночью: {night_temperature}
Температура днём: {day_temperature}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
        '''
        return result


def shymkent_after_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-shymkente/3-days/')
    html = BeautifulSoup(r.content, 'html.parser')

    for tomorrow in html.select('div._18iJ:nth-child(3)'):
        night_temperature = tomorrow.select_one('span._3k_D:nth-child(2)').text
        for determine_temperature in tomorrow.select('div._3wdR:nth-child(2)'):
            day_temperature = determine_temperature.select_one('span._3k_D').text
        for wind in tomorrow.select('div._1Y0B.wind'):
            wind_result = wind.select_one('span._1DZh').text.lower()
        for precipitation in tomorrow.select('div._1Y0B.precipitationProbability'):
            preciptation_result = precipitation.select_one('span._1DZh').text.lower()
        result = f'''\
Прогноз погоды на после завтра:
Температура ночью: {night_temperature}
Температура днём: {day_temperature}
Скорость ветра: {wind_result}
Осадки: {preciptation_result}
        '''
        return result
