from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

f = [[KeyboardButton(text='Зашифровать 🔑'), KeyboardButton(text='Расшифровать 🔐')]]#KeyboardButton(text='Настройки ⚙️')
encrkeyboard = [[KeyboardButton(text='Шифр Атбаш'), KeyboardButton(text='Шифр Цезаря'), KeyboardButton(text='Шифр Ришелье')]]
greet_kb = ReplyKeyboardMarkup(keyboard=f)
encrypt = ReplyKeyboardMarkup(keyboard=encrkeyboard)

def crypto_inline_greet():
    inline_kb_list = [
        [InlineKeyboardButton(text='🔙 Назад', callback_data='back')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)
#greet_kb.add(button_hi)