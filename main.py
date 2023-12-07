import telebot
from telebot import types

import kandinsky

bot = telebot.TeleBot('6688638137:AAHuaFIar3ePti4X_a7XsbYVUmPd2HG22fg')
prompt = ''


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Напишите текстовый запрос для Вашей картинки:')


@bot.message_handler()
def main(message):
    prompt = message.text
    bot.send_message(message.chat.id, 'Генерирую...')
    kandinsky.gen(prompt)
    pic = open('./image.jpeg', 'rb')
    markup = types.InlineKeyboardMarkup()
    buttonlike = types.InlineKeyboardButton('\U0001F44D', callback_data='save')
    buttondislike = types.InlineKeyboardButton('\U0001F44E', callback_data='delete')
    markup.row(buttonlike, buttondislike)
    bot.send_photo(message.chat.id, pic, reply_markup=markup, caption=f'Готово! Ваше изображение: "{prompt}"')
    bot.send_message(message.chat.id, 'Вы можете продолжить пользоваться ботом, просто введите еще один запрос:')


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'save':
        bot.send_message(callback.message.chat.id, 'Изображение сохранено!')
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)


bot.polling(none_stop=True)
