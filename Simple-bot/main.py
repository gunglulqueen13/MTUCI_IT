import telebot
import random
from telebot import types
from random import randint


token = "5065973391:AAG0eFLQRK4sNH_16aHnWTlzAiF0VljPmWk"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("покажи мой путь", "/start", "/help", "/WebM", "/luck", "/motivation")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id,
'''Здесь не так много функций, но:
"покажи мой путь" - ссылка на паблик МТУСИ
/help - список функций бота
/WebM - фильм из Ютуба
/luck - проверь свою удачу!!!!
/motivation - фраза дня
''')


@bot.message_handler(commands=['luck'])
def luck(message):
    bot.send_message(message.chat.id, 'Сомневаешься в выборе? Проверь свою удачу у нас!!!')
    luck_rand = randint(0, 100)
    str_output = "Вероятность того, что ты задумал, равна " + str(luck_rand) + " %"
    bot.send_message(message.chat.id, str_output)
    if luck_rand < 50:
        lil_buda = open('убили негра.mp3', 'rb')
        bot.send_voice(message.chat.id, lil_buda)


@bot.message_handler(commands=['WebM'])
def WebM(message):
    test_list = ["https://www.youtube.com/watch?v=whTjYy464cY", "https://www.youtube.com/watch?v=Isnr41HLcgU", "https://www.youtube.com/watch?v=cRYurR4kbTo"]
    random_index = random.choice(test_list)
    bot.send_message(message.chat.id, random_index)


@bot.message_handler(commands=['motivation'])
def phrase(message):
    phrases = open("phrases.txt", "rb")
    content_list = phrases.readlines()
    bot.send_message(message.chat.id, random.choice(content_list))


@bot.message_handler(content_types=['text'])
def echo_all(message):
    if message.text.lower() == "покажи мой путь":
        bot.send_message(message.chat.id, 'Тогда тебе сюда, юный подаван – https://mtuci.ru/')
        bot.send_photo(message.chat.id, open('bonjour.jpg', 'rb'))
    elif message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'спасибо':
        bot.send_message(message.chat.id, 'Всегда пожалуйста')
    else:
        bot.send_message(message.chat.id, message.text)

bot.polling()
