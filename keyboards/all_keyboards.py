from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

f = [[KeyboardButton(text='Зашифровать 🔑'), KeyboardButton(text='Расшифровать 🔐'), KeyboardButton(text='Настройки ⚙️')]]

greet_kb = ReplyKeyboardMarkup(keyboard=f)
#greet_kb.add(button_hi)