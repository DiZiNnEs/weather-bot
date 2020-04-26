import telebot
import pyowm

import parser

owm = pyowm.OWM('04b131cf413fc3c95dc41cb0d44326d0', language='ru')
bot = telebot.TeleBot("943137137:AAHUONQt5vh4ACwnsAgIur0IdtKAznbl_II")



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'''
Привет, {message.chat.username}👋.
Мое имя WeatherBot, я могу отправлять тебе результаты погоды из городов Казахстана)
Отправь мне название любого города и мигом отвечу тебе!
    ''', parse_mode='Markdown')


# @bot.message_handler(commands=['aktau'])
# def aktau(message):
#     observation = owm.weather_at_place('Aktau,KZ')
#     output = observation.get_weather()
#     bot.send_message(message.chat.id, f'''
# Температура Актау на сегодня: {output.get_temperature('celsius')['temp_max']} градусов по цельсий
# Влажность Актау на сегодня: {output.get_humidity()}%
# Скорость Ветра в Актау: {output.get_wind()['speed']} м/с
# Состояние погоды в общем: {output.get_detailed_status()}
# ''')
#
#
# @bot.message_handler(commands=['aktobe'])
# def aktobe(message):
#     observation = owm.weather_at_place('Aktobe,KZ')
#     output = observation.get_weather()
#     bot.send_message(message.chat.id, f'''
# Температура Актобе на сегодня: {output.get_temperature('celsius')['temp_max']} градусов по цельсий
# Влажность Актобе на сегодня: {output.get_humidity()}%
# Скорость Ветра в Актобе: {output.get_wind()['speed']} м/с
# Состояние погоды в общем: {output.get_detailed_status()}
#     ''')
#
#
# @bot.message_handler(commands=['almaty'])
# def almaty(message):
#     observation = owm.weather_at_place('Almaty,KZ')
#     output = observation.get_weather()
#     bot.send_message(message.chat.id, f'''
# Температура Алматы на сегодня: {output.get_temperature('celsius')['temp_max']} градусов по цельсий
# Влажность Алматы на сегодня: {output.get_humidity()}%
# Скорость Ветра в Алмате: {output.get_wind()['speed']} м/с
# Состояние погоды в общем: {output.get_detailed_status()}
#     ''')
#
#
# @bot.message_handler(commands=['atyrau'])
# def atyrau(message):
#     observation = owm.weather_at_place('Atyrau,KZ')
#     output = observation.get_weather()
#     bot.send_message(message.chat.id, f'''
# Температура Атырау на сегодня: {output.get_temperature('celsius')['temp_max']} градусов по цельсий
# Влажность Атырау на сегодня: {output.get_humidity()}%
# Скорость Ветра в Атырау: {output.get_wind()['speed']} м/с
# Состояние погоды в общем: {output.get_detailed_status()}
#     ''')
#
#
# @bot.message_handler(commands=['zhezkazgan'])
# def zhezkazgan(message):
#     observation = owm.weather_at_place('Zhezkazgan,KZ')
#     output = observation.get_weather()
#     bot.send_message(message.chat.id, f'''
# Температура Жезказган на сегодня: {output.get_temperature('celsius')['temp_max']} градусов по цельсий
# Влажность Жезказган на сегодня: {output.get_humidity()}%
# Скорость Ветра в Жезказгане: {output.get_wind()['speed']} м/с
# Состояние погоды в общем: {output.get_detailed_status()}
#     ''')
#
#
# @bot.message_handler(commands=['karagandy'])
# def karagandy(message):
#     observation = owm.weather_at_place('Karagandy,KZ')
#     output = observation.get_weather()
#     bot.send_message(message.chat.id, f'''
# Температура Караганды на сегодня: {output.get_temperature('celsius')['temp_max']} градусов по цельсий
# Влажность Караганды на сегодня: {output.get_humidity()}%
# Скорость Ветра в Караганде: {output.get_wind()['speed']} м/с
# Состояние погоды в общем: {output.get_detailed_status()}
#     ''')
#
#
# @bot.message_handler(commands=['kyzylorda'])
# def kyzylorda(message):
#     observation = owm.weather_at_place('Kyzylorda,KZ')
#     output = observation.get_weather()
#     bot.send_message(message.chat.id, f'''
# Температура Кызылорда на сегодня: {output.get_temperature('celsius')['temp_max']} градусов по цельсий
# Влажность Кызылорда на сегодня: {output.get_humidity()}%
# Скорость Ветра в Кызылорде: {output.get_wind()['speed']} м/с
# Состояние погоды в общем: {output.get_detailed_status()}
#     ''')
#
#
# @bot.message_handler(commands=['kokshetau'])
# def kokshetau(message):
#     observation = owm.weather_at_place('Kokshetau,KZ')
#     output = observation.get_weather()
#     bot.send_message(message.chat.id, f'''
# Температура Кокшетау на сегодня: {output.get_temperature('celsius')['temp_max']} градусов по цельсий
# Влажность Кокшетау на сегодня: {output.get_humidity()}%
# Скорость Ветра в Кокшетау: {output.get_wind()['speed']} м/с
# Состояние погоды в общем: {output.get_detailed_status()}
#     ''')
#
#
# @bot.message_handler(commands=['kostanay'])
# def kostanay(message):
#     observation = owm.weather_at_place('Kostanay,KZ')
#     output = observation.get_weather()
#     bot.send_message(message.chat.id, f'''
# Температура Костанай на сегодня: {output.get_temperature('celsius')['temp_max']} градусов по цельсий
# Влажность Костанай на сегодня: {output.get_humidity()}%
# Скорость Ветра в Костанае: {output.get_wind()['speed']} м/с
# Состояние погоды в общем: {output.get_detailed_status()}
#     ''')
#
#
# @bot.message_handler(commands=['nursultan'])
# def nursultan(message):
#     observation = owm.weather_at_place('Nur-Sultan,KZ')
#     output = observation.get_weather()
#     bot.send_message(message.chat.id, f'''
# Температура Нур-Султан на сегодня: {output.get_temperature('celsius')['temp_max']} градусов по цельсий
# Влажность Нур-Султан на сегодня: {output.get_humidity()}%
# Скорость Ветра в Нур-Султане: {output.get_wind()['speed']} м/с
# Состояние погоды в общем: {output.get_detailed_status()}
#     ''')
#
#
# @bot.message_handler(commands=['pavlodar'])
# def pavlodar(message):
#     observation = owm.weather_at_place('Pavlodar,KZ')
#     output = observation.get_weather()
#     bot.send_message(message.chat.id, f'''
# Температура Павлодар на сегодня: {output.get_temperature('celsius')['temp_max']} градусов по цельсий
# Влажность Павлодар на сегодня: {output.get_humidity()}%
# Скорость Ветра в Павлодаре: {output.get_wind()['speed']} м/с
# Состояние погоды в общем: {output.get_detailed_status()}
#     ''')
#
#
# @bot.message_handler(commands=['petropavl'])
# def petropavl(message):
#     observation = owm.weather_at_place('Petropavl,KZ')
#     output = observation.get_weather()
#     bot.send_message(message.chat.id, f'''
# Температура Петропавлск на сегодня: {output.get_temperature('celsius')['temp_max']} градусов по цельсий
# Влажность Петропавлс на сегодня: {output.get_humidity()}%
# Скорость Ветра в Петропавлоске: {output.get_wind()['speed']} м/с
# Состояние погоды в общем: {output.get_detailed_status()}
#     ''')
#
#
# @bot.message_handler(commands=['semey'])
# def semey(message):
#     observation = owm.weather_at_place('Semey,KZ')
#     output = observation.get_weather()
#     bot.send_message(message.chat.id, f'''
# Температура Семей на сегодня: {output.get_temperature('celsius')['temp_max']} градусов по цельсий
# Влажность Семей на сегодня: {output.get_humidity()}%
# Скорость Ветра в Семее: {output.get_wind()['speed']} м/с
# Состояние погоды в общем: {output.get_detailed_status()}
#     ''')
#
#
# @bot.message_handler(commands=['stepnogorsk'])
# def stepnogorsk(message):
#     observation = owm.weather_at_place('Stepnogorsk,KZ')
#     output = observation.get_weather()
#     bot.send_message(message.chat.id, f'''
# Температура Степнагорск на сегодня: {output.get_temperature('celsius')['temp_max']} градусов по цельсий
# Влажность Степнагорск на сегодня: {output.get_humidity()}%
# Скорость Ветра в Степнагорске: {output.get_wind()['speed']} м/с
# Состояние погоды в общем: {output.get_detailed_status()}
#     ''')
#
#
# @bot.message_handler(commands=['taldykorgan'])
# def taldykorgan(message):
#     observation = owm.weather_at_place('Taldykorgan,KZ')
#     output = observation.get_weather()
#     bot.send_message(message.chat.id, f'''
# Температура Талдыкорган на сегодня: {output.get_temperature('celsius')['temp_max']} градусов по цельсий
# Влажность Талдыкорган на сегодня: {output.get_humidity()}%
# Скорость Ветра в Талдыркоргане: {output.get_wind()['speed']} м/с
# Состояние погоды в общем: {output.get_detailed_status()}
#     ''')
#
#
# @bot.message_handler(commands=['temirtau'])
# def temirtau(message):
#     observation = owm.weather_at_place('Temirtau,KZ')
#     output = observation.get_weather()
#     bot.send_message(message.chat.id, f'''
# Температура Темиртау на сегодня: {output.get_temperature('celsius')['temp_max']} градусов по цельсий
# Влажность Темиртау на сегодня: {output.get_humidity()}%
# Скорость Ветра в Темиртау: {output.get_wind()['speed']} м/с
# Состояние погоды в общем: {output.get_detailed_status()}
#     ''')
#
#
# @bot.message_handler(commands=['oskemen'])
# def oskemen(message):
#     observation = owm.weather_at_place('Oskemen,KZ')
#     output = observation.get_weather()
#     bot.send_message(message.chat.id, f'''
# Температура Оскемен на сегодня: {output.get_temperature('celsius')['temp_max']} градусов по цельсий
# Влажность Оскемен на сегодня: {output.get_humidity()}%
# Скорость Ветра в Оскемене: {output.get_wind()['speed']} м/с
# Состояние погоды в общем: {output.get_detailed_status()}
#     ''')
#
#
# @bot.message_handler(commands=['shymkent'])
# def shymkent(message):
#     observation = owm.weather_at_place('Shymkent,KZ')
#     output = observation.get_weather()
#     bot.send_message(message.chat.id, f'''
# Температура Шымкент на сегодня: {output.get_temperature('celsius')['temp_max']} градусов по цельсий
# Влажность Шымкент на сегодня: {output.get_humidity()}%
# Скорость Ветра в Шымкенте: {output.get_wind()['speed']} м/с
# Состояние погоды в общем: {output.get_detailed_status()}
#     ''')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, f'''
Введите любой из предложенных городов Казахстана, к примеру:
/nursultan - выведит всю информацию о погоде города Нур-Султан
Информация о погоде берется с https://openweathermap.org/
''')


def weather_about(city):
    observation = owm.weather_at_place(city)
    output = observation.get_weather()
    information = (f'''
Информацию о погоде в городе {city}
Температура на сегодня: {output.get_temperature('celsius')['temp_max']}° по цельсий
Влажность воздуха: {output.get_humidity()}%
Скорость ветра: {output.get_wind()['speed']} м/с
Состояние погоды в общем: {output.get_detailed_status()}
''')
    return information


@bot.message_handler(content_types=['text'])
def city(message):
    if message.text.lower() == 'актау':
        bot.send_message(message.chat.id, weather_about('Актау'))
    elif message.text.lower() == 'актобе':
        bot.send_message(message.chat.id, weather_about('Актобе'))
    elif message.text.lower() == 'алматы' or message.text.lower() == 'алмата':
        bot.send_message(message.chat.id, weather_about('Алматы'))
    elif message.text.lower() == 'атырау':
        bot.send_message(message.chat.id, weather_about('Атырау'))
    elif message.text.lower() == 'жезказган':
        bot.send_message(message.chat.id, weather_about('Жезказган'))
    elif message.text.lower() == 'караганда':
        bot.send_message(message.chat.id, weather_about('Караганда'))
    elif message.text.lower() == 'кызылорда':
        bot.send_message(message.chat.id, weather_about('Кызылорда'))
    elif message.text.lower() == 'кокшетау':
        bot.send_message(message.chat.id, weather_about('Кокшетау'))
    elif message.text.lower() == 'костанай':
        bot.send_message(message.chat.id, weather_about('Костанай'))
    elif message.text.lower() == 'нур-султан' or message.text.lower() == 'астана':
        bot.send_message(message.chat.id, weather_about('Нур-Султан'))
        bot.send_message(message.chat.id, parser.nursultan_parser())
    elif message.text.lower() == 'павлодар':
        bot.send_message(message.chat.id, weather_about('Павлодар'))
    elif message.text.lower() == 'петропавловск':
        bot.send_message(message.chat.id, weather_about('Петропавловск'))
    elif message.text.lower() == 'семей':
        bot.send_message(message.chat.id, weather_about('Семей'))
    elif message.text.lower() == 'степнагорск':
        bot.send_message(message.chat.id, weather_about('Степнагорск'))
    elif message.text.lower() == 'талдыкорган':
        bot.send_message(message.chat.id, weather_about('Талдыкорган'))
    elif message.text.lower() == 'темиртау':
        bot.send_message(message.chat.id, weather_about('Темиртау'))
    elif message.text.lower() == 'усть-каменогорск' or message.text.lower() == 'оскемен':
        bot.send_message(message.chat.id, weather_about('Усть-Каменогорск'))
    elif message.text.lower() == 'шымкент':
        bot.send_message(message.chat.id, weather_about('Шымкент'))
    else:
        bot.send_message(message.chat.id, 'Извините, я вас не понимаю, введите /help')

bot.polling()
