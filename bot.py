
import telebot
from telebot import types

TOKEN = '***'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def hello_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_1 = types.KeyboardButton("Выйди из чата")
    item_2 = types.KeyboardButton("Статистика по чату")
    markup.add(item_1, item_2)
    bot.send_message(message.chat.id, "Саламулейкум дорогой друг", reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    text = '''
/ban - ответь этим на сообщение того, кого забанить(не должен быть админом)
/start - начать и вызвать функции по чату
/cat - фотки мурок
/help - это сообщение
    '''
    bot.send_message(message.chat.id, text)



@bot.message_handler(commands=['cat'])
def cat(message):
    b1 = types.KeyboardButton("Серый")
    b2 = types.KeyboardButton("Рыжий")
    b3 = types.KeyboardButton("Черный")
    b4 = types.KeyboardButton("Белый")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add(b1, b2, b3, b4)
    text = '''
    Мейн-кун – аборигенная порода американских кошек, 
характеризующаяся крупными размерами и внушительной массой тела. Представители 
породы – это надежные друзья и компаньоны, способные быстро завоевать любовь всей семьи.'''
    bot.send_message(message.chat.id, "Мурки", reply_markup=markup)
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(content_types=['new_chat_members'])
def hey(message):
    bot.send_message(message.chat.id, "Саламулейкум дорогой друг")


@bot.message_handler(commands=["ban"])
def ban_user(message):
    try:
        bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        bot.send_message(message.chat.id, "done")
    except Exception as e:
        bot.send_message(message.chat.id, e)
        bot.send_message(message.chat.id, 'ответьте на сообщение осужденного')
        bot.send_message(message.chat.id, 'он не должен быть админом')

    # bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == 'Чурка' or message.text == 'Хач':
        bot.send_message(chat_id=message.chat.id, text='сам ты ' + message.text)
    if message.text == 'Выйди из чата':
        bot.leave_chat(message.chat.id)
    if message.text == 'Статистика по чату':
        users = bot.get_chat_member_count(message.chat.id)
        admins = len(bot.get_chat_administrators(message.chat.id))
        text = f'пользователей в чате: {users} \nадминов в чате: {admins}'
        bot.send_message(message.chat.id, text)
    if message.text == 'Серый':
        cat_1 = 'https://krasivosti.pro/uploads/posts/2021-06/1623483458_6-krasivosti_pro-p-mein-kun-serii-zhivotnie-krasivo-foto-6.jpg'
        bot.send_photo(message.chat.id, cat_1)
    if message.text == 'Рыжий':
        cat_2 = 'https://oir.mobi/uploads/posts/2021-05/1621494979_12-oir_mobi-p-mein-kun-rizhii-bolshoi-zhivotnie-krasivo-14.jpg'
        bot.send_photo(message.chat.id, cat_2)
    if message.text == 'Черный':
        cat_3 = 'https://funart.pro/uploads/posts/2021-07/1627509133_3-funart-pro-p-chernie-mein-kuni-zhivotnie-krasivo-foto-3.jpg'
        bot.send_photo(message.chat.id, cat_3)
    if message.text == 'Белый':
        cat_4 = 'https://funart.pro/uploads/posts/2021-07/1626890244_10-funart-pro-p-belii-mein-kun-s-golubimi-glazami-zhivotni-12.jpg'
        bot.send_photo(message.chat.id, cat_4)


bot.polling(none_stop=True, interval=0)
