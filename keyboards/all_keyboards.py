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
    f = [[InlineKeyboardButton(text='📊 Частотный криптоанализ', callback_data = 'cryptoanalysis')],
         [InlineKeyboardButton(text='🔒 Шифр', callback_data = 'encrypt')],
         [InlineKeyboardButton(text='💬 Сообщение', callback_data='msg')],
         [InlineKeyboardButton(text='🗝 Ключ',callback_data='key')],
         [InlineKeyboardButton(text='🔙 Назад', callback_data = 'back')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=f)
def settings_encrypt_inline():
    f = [[InlineKeyboardButton(text='🕍 Шифр Атбаш', callback_data = 'atbash')],
         [InlineKeyboardButton(text='👑 Шифр Цезаря', callback_data='caesar')],
         [InlineKeyboardButton(text='🎎 Шифр Ришелье',callback_data='richeliu')],
         [InlineKeyboardButton(text='⚔️ Шифр Гронсфельда', callback_data='gronsfeld')],
         [InlineKeyboardButton(text='⚗️ Шифр Виженера', callback_data='vigenere')],
         [InlineKeyboardButton(text='⚛️ Шифр Плейфера', callback_data='playfair')],
         [InlineKeyboardButton(text='🔙 Назад', callback_data = 'settings')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=f)
def crypto_inline_greet():
    inline_kb_list = [
        [InlineKeyboardButton(text='🔙 Назад', callback_data='back')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)
def crypto_inline_change_text_params():
    inline_kb_list = [
        [InlineKeyboardButton(text='🔙 Замена символов в тексте', callback_data='change')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)