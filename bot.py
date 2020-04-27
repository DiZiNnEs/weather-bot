import telebot
import pyowm

import tomorrow_parser
import after_tomorrow_parser

owm = pyowm.OWM('04b131cf413fc3c95dc41cb0d44326d0', language='ru')
bot = telebot.TeleBot("943137137:AAHUONQt5vh4ACwnsAgIur0IdtKAznbl_II")


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'''
Привет, {message.chat.username}👋.
Мое имя WeatherBot, я могу отправлять тебе результаты погоды из городов Казахстана🇰🇿
Отправь мне название любого города и мигом отвечу тебе!
    ''', parse_mode='Markdown')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, f'''
Введите любой из предложенных городов Казахстана🇰🇿, к примеру:
Актау - выведит всю информацию о погоде города Актау
Информация о сегодняшней погоде берется с:  https://openweathermap.org/
Информация о завтрашней и после завтрашней погоде берется с: https://weather.rambler.ru/world/kazakhstan/
''')


@bot.message_handler(commands=['list'])
def list(message):
    bot.send_message(message.chat.id, f'''
Доступны следующие города:
1. Актау
2. Актобе
3. Алмата
4. Атырау
5. Жезказган
6. Караганда
7. Кызылорда
8. Кокшетау
9. Костанай
10. Нур-Султан (Астана)
11. Павлодар
12. Петропавловск
13. Семипалатинкс
14. Степногорск
15. Талдыкорган
16. Темиртау
17. Усть-Каменогорск
18. Шымкент
''')


def weather_about(city):
    observation = owm.weather_at_place(city)
    output = observation.get_weather()
    information = (f'''\
Информацию о погоде на сегодня в городе {city}:
Температура на сегодня🌕: {output.get_temperature('celsius')['temp_max']}° по цельсий
Влажность воздуха🌫: {output.get_humidity()}%
Скорость ветра💨: {output.get_wind()['speed']} м/с
Состояние погоды в общем: {output.get_detailed_status()}
''')
    return information


@bot.message_handler(content_types=['text'])
def city(message):
    if message.text.lower() == 'актау':
        bot.send_message(message.chat.id, weather_about('Актау'))
        bot.send_message(message.chat.id, tomorrow_parser.aktau_tomorrow_parser())
        bot.send_message(message.chat.id, after_tomorrow_parser.aktau_after_tomorrow_parser())

    elif message.text.lower() == 'актобе':
        bot.send_message(message.chat.id, weather_about('Актобе'))
        bot.send_message(message.chat.id, tomorrow_parser.aktobe_tomorrow_parser())
        bot.send_message(message.chat.id, after_tomorrow_parser.aktobe_after_tomorrow_parser())

    elif message.text.lower() == 'алматы' or message.text.lower() == 'алмата':
        bot.send_message(message.chat.id, weather_about('Алматы'))
        bot.send_message(message.chat.id, tomorrow_parser.almaty_tomorrow_parser())
        bot.send_message(message.chat.id, after_tomorrow_parser.almaty_after_tomorrow_parser())

    elif message.text.lower() == 'атырау':
        bot.send_message(message.chat.id, weather_about('Атырау'))
        bot.send_message(message.chat.id, tomorrow_parser.atyrau_tomorrow_parser())
        bot.send_message(message.chat.id, after_tomorrow_parser.atyrau_after_tomorrow_parser())

    elif message.text.lower() == 'жезказган':
        bot.send_message(message.chat.id, weather_about('Жезказган'))
        bot.send_message(message.chat.id, tomorrow_parser.zhezkazgan_tomorrow_parser())
        bot.send_message(message.chat.id, after_tomorrow_parser.zhezkazgan_after_tomorrow_parser())

    elif message.text.lower() == 'караганда':
        bot.send_message(message.chat.id, weather_about('Караганда'))
        bot.send_message(message.chat.id, tomorrow_parser.karaganda_tomorrow_parser())
        bot.send_message(message.chat.id, after_tomorrow_parser.karaganda_after_tomorrow_parser())

    elif message.text.lower() == 'кызылорда':
        bot.send_message(message.chat.id, weather_about('Кызылорда'))
        bot.send_message(message.chat.id, tomorrow_parser.kyzylorda_tomorrow_parser())
        bot.send_message(message.chat.id, after_tomorrow_parser.kyzylorda_after_tomorrow_parser())

    elif message.text.lower() == 'кокшетау':
        bot.send_message(message.chat.id, weather_about('Кокшетау'))
        bot.send_message(message.chat.id, tomorrow_parser.kokshetau_tomorrow_parser())
        bot.send_message(message.chat.id, after_tomorrow_parser.kokshetau_after_tomorrow_parser())

    elif message.text.lower() == 'костанай':
        bot.send_message(message.chat.id, weather_about('Костанай'))
        bot.send_message(message.chat.id, tomorrow_parser.kostanai_tomorrow_parser())
        bot.send_message(message.chat.id, after_tomorrow_parser.kostanai_after_tomorrow_parser())

    elif message.text.lower() == 'нур-султан' or message.text.lower() == 'астана':
        bot.send_message(message.chat.id, weather_about('Нур-Султан'))
        bot.send_message(message.chat.id, tomorrow_parser.nursultan_tomorrow_parser())
        bot.send_message(message.chat.id, after_tomorrow_parser.nursultan_after_tomorrow_parser())

    elif message.text.lower() == 'павлодар':
        bot.send_message(message.chat.id, weather_about('Павлодар'))
        bot.send_message(message.chat.id, tomorrow_parser.pavlodar_tomorrow_parser())
        bot.send_message(message.chat.id, after_tomorrow_parser.pavlodar_after_tomorrow_parser())

    elif message.text.lower() == 'петропавловск' or message.text.lower() == 'петропавл':
        bot.send_message(message.chat.id, weather_about('Петропавловск'))
        bot.send_message(message.chat.id, tomorrow_parser.petropavlovsk_tomorrow_parser())
        bot.send_message(message.chat.id, after_tomorrow_parser.petropavlovsk_after_tomorrow_parser())

    elif message.text.lower() == 'семей' or message.text.lower() == 'семипалатинск':
        bot.send_message(message.chat.id, weather_about('Семей'))
        bot.send_message(message.chat.id, tomorrow_parser.semipalatinsk_tomorrow_parser())
        bot.send_message(message.chat.id, after_tomorrow_parser.semipalatinsk_after_tomorrow_parser())

    elif message.text.lower() == 'степногорск':
        bot.send_message(message.chat.id, weather_about('Степногорск'))
        bot.send_message(message.chat.id, tomorrow_parser.stepnogorsk_tomorrow_parser())
        bot.send_message(message.chat.id, after_tomorrow_parser.stepnogorsk_after_tomorrow_parser())

    elif message.text.lower() == 'талдыкорган':
        bot.send_message(message.chat.id, weather_about('Талдыкорган'))
        bot.send_message(message.chat.id, tomorrow_parser.taldykorgan_tomorrow_parser())
        bot.send_message(message.chat.id, after_tomorrow_parser.taldykorgan_after_tomorrow_parser())

    elif message.text.lower() == 'темиртау':
        bot.send_message(message.chat.id, weather_about('Темиртау'))
        bot.send_message(message.chat.id, tomorrow_parser.temirtau_tomorrow_parser())
        bot.send_message(message.chat.id, after_tomorrow_parser.temirtau_after_tomorrow_parser())

    elif message.text.lower() == 'усть-каменогорск' or message.text.lower() == 'оскемен':
        bot.send_message(message.chat.id, weather_about('Усть-Каменогорск'))
        bot.send_message(message.chat.id, tomorrow_parser.oskemen_tomorrow_parser())
        bot.send_message(message.chat.id, after_tomorrow_parser.oskemen_after_tomorrow_parser())

    elif message.text.lower() == 'шымкент':
        bot.send_message(message.chat.id, weather_about('Шымкент'))
        bot.send_message(message.chat.id, tomorrow_parser.shymkent_tomorrow_parser())
        bot.send_message(message.chat.id, after_tomorrow_parser.shymkent_after_tomorrow_parser())

    else:
        bot.send_message(message.chat.id, 'Извините, я вас не понимаю, введите /help')


bot.polling()
