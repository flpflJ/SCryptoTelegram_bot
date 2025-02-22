from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

f = [[KeyboardButton(text='Зашифровать 🔑'), KeyboardButton(text='Расшифровать 🔐'), KeyboardButton(text='Настройки ⚙️')]]

greet_kb = ReplyKeyboardMarkup(keyboard=f)

def crypto_inline_greet():
    inline_kb_list = [
        [InlineKeyboardButton(text='Сообщение', callback_data='cryptmesg')]
    ]
#greet_kb.add(button_hi)