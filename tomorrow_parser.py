import requests

from bs4 import BeautifulSoup
from textwrap import dedent


def aktau_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-aktau-mangistauskoy-oblasti/3-days/')
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


def aktobe_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-aktobe/3-days/')
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


def almaty_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-almaty/3-days/')
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


def atyrau_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-atyrau/3-days/')
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


def zhezkazgan_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-zhezkazgane-dzhezkazgane/3-days/')
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


def karaganda_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-karagande/3-days/')
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


def kyzylorda_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-kyzylorde/3-days/')
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


def kokshetau_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-kokshetau/3-days/')
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


def kostanai_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-kostanae/3-days/')
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


def nursultan_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-nur-sultane/3-days/')
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


def pavlodar_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-pavlodare/3-days/')
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


def petropavlovsk_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-petropavlovske/3-days/')
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


def semipalatinsk_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-semipalatinske/3-days/')
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


def stepnogorsk_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-stepnogorske/3-days/')
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


def taldykorgan_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-taldykorgane/3-days/')
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


def temirtau_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-temirtau/kazakhstan/3-days/')
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


def oskemen_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-ust-kamenogorske/3-days/')
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


def shymkent_tomorrow_parser():
    r = requests.get('https://weather.rambler.ru/v-shymkente/3-days/')
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
