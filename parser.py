import requests

from bs4 import BeautifulSoup
from textwrap import dedent


def today_parser(city):
    r = requests.get(city)
    html = BeautifulSoup(r.content, 'html.parser')
    today = html.select_one('div._18iJ:nth-child(1)')
    night_temperature = today.select_one('span._3k_D:nth-child(2)').text
    determine_temperature = today.select_one('div._3wdR:nth-child(2)')
    day_temperature = determine_temperature.select_one('span._3k_D').text
    wind = today.select_one('div._1Y0B.wind')
    wind_result = wind.select_one('span._1DZh').text.lower()
    precipitation = today.select_one('div._1Y0B.precipitationProbability')
    precipitation_select = precipitation.select_one('span._1DZh')
    all_precipitation = precipitation_select.select_one('span')

    if all_precipitation is not None:
        precipitation_output = [e.strip() for e in all_precipitation if not e.name and e.strip()][0]
    else:
        precipitation_output = None

    result = dedent(f'''
                  Прогноз погоды на сегодня:
                  Температура ночью🌑: {night_temperature} по цельсию
                  Температура днём🌕: {day_temperature} по цельсию
                  Скорость ветра💨: {wind_result}
                  Осадки🌧: {f'вероятность осадков {precipitation_output}%☔️' if precipitation_output is not None else 'без осадков☂️'}
              ''')
    return result


def tomorrow_parser(city):
    r = requests.get(city)
    html = BeautifulSoup(r.content, 'html.parser')
    tomorrow = html.select_one('div._18iJ:nth-child(2)')
    night_temperature = tomorrow.select_one('span._3k_D:nth-child(2)').text
    determine_temperature = tomorrow.select_one('div._3wdR:nth-child(2)')
    day_temperature = determine_temperature.select_one('span._3k_D').text
    wind = tomorrow.select_one('div._1Y0B.wind')
    wind_result = wind.select_one('span._1DZh').text.lower()
    precipitation = tomorrow.select_one('div._1Y0B.precipitationProbability')
    precipitation_select = precipitation.select_one('span._1DZh')
    all_precipitation = precipitation_select.select_one('span')

    if all_precipitation is not None:
        precipitation_output = [e.strip() for e in all_precipitation if not e.name and e.strip()][0]
    else:
        precipitation_output = None

    result = dedent(f'''
            Прогноз погоды на завтра:
            Температура ночью🌑: {night_temperature} по цельсию
            Температура днём🌕: {day_temperature} по цельсию
            Скорость ветра💨: {wind_result}
            Осадки🌧: {f'вероятность осадков {precipitation_output}%☔️' if precipitation_output is not None else 'без осадков☂️'}
        ''')
    return result


def after_tomorrow_parser(city):
    r = requests.get(city)
    html = BeautifulSoup(r.content, 'html.parser')
    after_tomorrow = html.select_one('div._18iJ:nth-child(3)')
    night_temperature = after_tomorrow.select_one('span._3k_D:nth-child(2)').text
    determine_temperature = after_tomorrow.select_one('div._3wdR:nth-child(2)')
    day_temperature = determine_temperature.select_one('span._3k_D').text
    wind = after_tomorrow.select_one('div._1Y0B.wind')
    wind_result = wind.select_one('span._1DZh').text.lower()
    precipitation = after_tomorrow.select_one('div._1Y0B.precipitationProbability')
    precipitation_select = precipitation.select_one('span._1DZh')
    all_precipitation = precipitation_select.select_one('span')

    if all_precipitation is not None:
        precipitation_output = [e.strip() for e in all_precipitation if not e.name and e.strip()][0]
    else:
        precipitation_output = None

    result = dedent(f'''
                Прогноз погоды на после завтра:
                Температура ночью🌑: {night_temperature} по цельсию
                Температура днём🌕: {day_temperature} по цельсию
                Скорость ветра💨: {wind_result}
                Осадки🌧: {f'вероятность осадков {precipitation_output}%☔️' if precipitation_output is not None else 'без осадков☂️'}
            ''')
    return result