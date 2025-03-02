from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
def inline_greet():
    f = [[InlineKeyboardButton(text='Зашифровать 🔑', callback_data = 'encrypto')],
          [InlineKeyboardButton(text='Расшифровать 🔐', callback_data = 'decrypt')],
          [InlineKeyboardButton(text='Настройки ⚙️', callback_data = 'settings')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=f)
def settings_inline():
    f = [[InlineKeyboardButton(text='🔒 Шифр', callback_data = 'encrypt')],
         [InlineKeyboardButton(text='💬 Сообщение', callback_data='msg')],
         [InlineKeyboardButton(text='🗝 Ключ',callback_data='key')],
         [InlineKeyboardButton(text='🔙 Назад', callback_data = 'back')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=f)
def settings_encrypt_inline():
    f = [[InlineKeyboardButton(text='🕍 Шифр Атбаш', callback_data = 'atbash')],
         [InlineKeyboardButton(text='👑 Шифр Цезаря', callback_data='caesar')],
         [InlineKeyboardButton(text='🎎 Шифр Ришелье',callback_data='richeliu')],
         [InlineKeyboardButton(text='🔙 Назад', callback_data = 'settings')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=f)
def crypto_inline_greet():
    inline_kb_list = [
        [InlineKeyboardButton(text='🔙 Назад', callback_data='back')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)