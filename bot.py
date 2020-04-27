import telebot

import parser

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


@bot.message_handler(content_types=['text'])
def city(message):
    if message.text.lower() == 'актау':
        bot.send_message(message.chat.id, parser.today_parser('https://weather.rambler.ru/v-aktau-mangistauskoy-oblasti/3-days/'))
        bot.send_message(message.chat.id, parser.tomorrow_parser('https://weather.rambler.ru/v-aktau-mangistauskoy-oblasti/3-days/'))
        bot.send_message(message.chat.id, parser.after_tomorrow_parser('https://weather.rambler.ru/v-aktau-mangistauskoy-oblasti/3-days/'))

    elif message.text.lower() == 'актобе':
        bot.send_message(message.chat.id, parser.today_parser('https://weather.rambler.ru/v-aktobe/3-days/'))
        bot.send_message(message.chat.id, parser.tomorrow_parser('https://weather.rambler.ru/v-aktobe/3-days/'))
        bot.send_message(message.chat.id, parser.after_tomorrow_parser('https://weather.rambler.ru/v-aktobe/3-days/'))

    elif message.text.lower() == 'алматы' or message.text.lower() == 'алмата':
        bot.send_message(message.chat.id, parser.today_parser('https://weather.rambler.ru/v-almaty/3-days/'))
        bot.send_message(message.chat.id, parser.tomorrow_parser('https://weather.rambler.ru/v-almaty/3-days/'))
        bot.send_message(message.chat.id, parser.after_tomorrow_parser('https://weather.rambler.ru/v-almaty/3-days/'))

    elif message.text.lower() == 'атырау':
        bot.send_message(message.chat.id, parser.today_parser('https://weather.rambler.ru/v-atyrau/3-days/'))
        bot.send_message(message.chat.id, parser.tomorrow_parser('https://weather.rambler.ru/v-atyrau/3-days/'))
        bot.send_message(message.chat.id, parser.after_tomorrow_parser('https://weather.rambler.ru/v-atyrau/3-days/'))

    elif message.text.lower() == 'жезказган':
        bot.send_message(message.chat.id, parser.today_parser('https://weather.rambler.ru/v-zhezkazgane-dzhezkazgane/3-days/'))
        bot.send_message(message.chat.id, parser.tomorrow_parser('https://weather.rambler.ru/v-zhezkazgane-dzhezkazgane/3-days/'))
        bot.send_message(message.chat.id, parser.after_tomorrow_parser('https://weather.rambler.ru/v-zhezkazgane-dzhezkazgane/3-days/'))

    elif message.text.lower() == 'караганда':
        bot.send_message(message.chat.id, parser.today_parser('https://weather.rambler.ru/v-karagande/3-days/'))
        bot.send_message(message.chat.id, parser.tomorrow_parser('https://weather.rambler.ru/v-karagande/3-days/'))
        bot.send_message(message.chat.id, parser.after_tomorrow_parser('https://weather.rambler.ru/v-karagande/3-days/'))

    elif message.text.lower() == 'кызылорда':
        bot.send_message(message.chat.id, parser.today_parser('https://weather.rambler.ru/v-kyzylorde/3-days/'))
        bot.send_message(message.chat.id, parser.tomorrow_parser('https://weather.rambler.ru/v-kyzylorde/3-days/'))
        bot.send_message(message.chat.id, parser.after_tomorrow_parser('https://weather.rambler.ru/v-kyzylorde/3-days/'))

    elif message.text.lower() == 'кокшетау':
        bot.send_message(message.chat.id, parser.today_parser('https://weather.rambler.ru/v-kokshetau/3-days/'))
        bot.send_message(message.chat.id, parser.tomorrow_parser('https://weather.rambler.ru/v-kokshetau/3-days/'))
        bot.send_message(message.chat.id, parser.after_tomorrow_parser('https://weather.rambler.ru/v-kokshetau/3-days/'))

    elif message.text.lower() == 'костанай':
        bot.send_message(message.chat.id, parser.today_parser('https://weather.rambler.ru/v-kostanae/3-days/'))
        bot.send_message(message.chat.id, parser.tomorrow_parser('https://weather.rambler.ru/v-kostanae/3-days/'))
        bot.send_message(message.chat.id, parser.after_tomorrow_parser('https://weather.rambler.ru/v-kostanae/3-days/'))

    elif message.text.lower() == 'нур-султан' or message.text.lower() == 'астана':
        bot.send_message(message.chat.id, parser.today_parser('https://weather.rambler.ru/v-nur-sultane/3-days/'))
        bot.send_message(message.chat.id, parser.tomorrow_parser('https://weather.rambler.ru/v-nur-sultane/3-days/'))
        bot.send_message(message.chat.id, parser.after_tomorrow_parser('https://weather.rambler.ru/v-nur-sultane/3-days/'))

    elif message.text.lower() == 'павлодар':
        bot.send_message(message.chat.id, parser.today_parser('https://weather.rambler.ru/v-pavlodare/3-days/'))
        bot.send_message(message.chat.id, parser.tomorrow_parser('https://weather.rambler.ru/v-pavlodare/3-days/'))
        bot.send_message(message.chat.id, parser.after_tomorrow_parser('https://weather.rambler.ru/v-pavlodare/3-days/'))

    elif message.text.lower() == 'петропавловск' or message.text.lower() == 'петропавл':
        bot.send_message(message.chat.id, parser.today_parser('https://weather.rambler.ru/v-petropavlovske/3-days/'))
        bot.send_message(message.chat.id, parser.tomorrow_parser('https://weather.rambler.ru/v-petropavlovske/3-days/'))
        bot.send_message(message.chat.id, parser.after_tomorrow_parser('https://weather.rambler.ru/v-petropavlovske/3-days/'))

    elif message.text.lower() == 'семей' or message.text.lower() == 'семипалатинск':
        bot.send_message(message.chat.id, parser.today_parser('https://weather.rambler.ru/v-semipalatinske/3-days/'))
        bot.send_message(message.chat.id, parser.tomorrow_parser('https://weather.rambler.ru/v-semipalatinske/3-days/'))
        bot.send_message(message.chat.id, parser.after_tomorrow_parser('https://weather.rambler.ru/v-semipalatinske/3-days/'))

    elif message.text.lower() == 'степногорск':
        bot.send_message(message.chat.id, parser.today_parser('https://weather.rambler.ru/v-stepnogorske/3-days/'))
        bot.send_message(message.chat.id, parser.tomorrow_parser('https://weather.rambler.ru/v-stepnogorske/3-days/'))
        bot.send_message(message.chat.id, parser.after_tomorrow_parser('https://weather.rambler.ru/v-stepnogorske/3-days/'))

    elif message.text.lower() == 'талдыкорган':
        bot.send_message(message.chat.id, parser.today_parser('https://weather.rambler.ru/v-taldykorgane/3-days/'))
        bot.send_message(message.chat.id, parser.tomorrow_parser('https://weather.rambler.ru/v-taldykorgane/3-days/'))
        bot.send_message(message.chat.id, parser.after_tomorrow_parser('https://weather.rambler.ru/v-taldykorgane/3-days/'))

    elif message.text.lower() == 'темиртау':
        bot.send_message(message.chat.id, parser.today_parser('https://weather.rambler.ru/v-temirtau/kazakhstan/3-days/'))
        bot.send_message(message.chat.id, parser.tomorrow_parser('https://weather.rambler.ru/v-temirtau/kazakhstan/3-days/'))
        bot.send_message(message.chat.id, parser.after_tomorrow_parser('https://weather.rambler.ru/v-temirtau/kazakhstan/3-days/'))

    elif message.text.lower() == 'усть-каменогорск' or message.text.lower() == 'оскемен':
        bot.send_message(message.chat.id, parser.today_parser('https://weather.rambler.ru/v-ust-kamenogorske/3-days/'))
        bot.send_message(message.chat.id, parser.tomorrow_parser('https://weather.rambler.ru/v-ust-kamenogorske/3-days/'))
        bot.send_message(message.chat.id, parser.after_tomorrow_parser('https://weather.rambler.ru/v-ust-kamenogorske/3-days/'))

    elif message.text.lower() == 'шымкент':
        bot.send_message(message.chat.id, parser.today_parser('https://weather.rambler.ru/v-shymkente/3-days/'))
        bot.send_message(message.chat.id, parser.tomorrow_parser('https://weather.rambler.ru/v-shymkente/3-days/'))
        bot.send_message(message.chat.id, parser.after_tomorrow_parser('https://weather.rambler.ru/v-shymkente/3-days/'))
    else:
        bot.send_message(message.chat.id, 'Извините, я вас не понимаю, введите /help')


bot.polling()
