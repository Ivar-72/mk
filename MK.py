import telebot
import config
import pb
import datetime
import pytz
import json
import traceback

P_TIMEZONE = pytz.timezone(config.TIMEZONE)
TIMEZONE_COMMON_NAME = config.TIMEZONE_COMMON_NAME

bot = telebot.TeleBot(config.TOKEN)



@bot.message_handler(commands=['Начать'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        'Готов узнать кто ты из шиноби мира МК?.\n'
    )
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Si', callback_data='Si'),
        telebot.types.InlineKeyboardButton('Нет', callback_data='Нет')
    )
    bot.send_message(
        message.chat.id,
        'Сделайте свой выбор:',
        reply_markup=keyboard
    )


@bot.message_handler(commands=['help'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Message the developer', url=''
  )
    )
    bot.send_message(
        message.chat.id,
        '1) To receive a list of available currencies press /exchange.\n' +
        '2) Click on the currency you are interested in.\n' +
        '3) You will receive a message containing information regarding the source and the target currencies, ' +
        'buying rates and selling rates.\n' +
        '4) Click “Update” to receive the current information regarding the request. ' +
        'The bot will also show the difference between the previous and the current exchange rates.\n' +
        '5) The bot supports inline. Type @<botusername> in any chat and the first letters of a currency.',
        reply_markup=keyboard
    )


@bot.message_handler(commands=['color'])
def exchange_command(message):
    bot.send_message(
        message.chat.id,
        'Ваш любимый цвет?'
    )
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Красный', callback_data='Красный'),
        telebot.types.InlineKeyboardButton('Серый', callback_data='Серый'),
        telebot.types.InlineKeyboardButton('Желтый', callback_data='Желтый'),
        telebot.types.InlineKeyboardButton('Cиний', callback_data='Cиний'),
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Зеленый', callback_data='Зеленый'),
        telebot.types.InlineKeyboardButton('Фиолетовый', callback_data='Фиолетовый'),
        telebot.types.InlineKeyboardButton('Черный', callback_data='Черный'),
        telebot.types.InlineKeyboardButton('Коричневый', callback_data='Коричневый'),

    )

    bot.send_message(
        message.chat.id,
        'Сделайте свой выбор:',
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data.startswith('Si'):
        print(data)
        bot.answer_inline_query(
            inline_query.id,
            get_iq_articles(pb.get_exchanges(inline_query.query))
        )


def get_ex_callback(query):
    bot.answer_callback_query(query.id)
    send_exchange_result(query.message, query.data)


def send_exchange_result(message, ex_code):
    bot.send_chat_action(message.chat.id, 'typing')
    # ex = pb.get_exchange(ex_code)
    bot.send_message(
        message.chat.id,
        reply_markup=get_update_keyboard(ex),
        parse_mode='HTML'
    )





bot.polling(none_stop=True)