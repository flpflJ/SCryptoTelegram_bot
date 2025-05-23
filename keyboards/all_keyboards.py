from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
def inline_greet():
    f = [[InlineKeyboardButton(text='Зашифровать 🔑', callback_data = 'encrypto')],
          [InlineKeyboardButton(text='Расшифровать 🔐', callback_data = 'decrypt')],
         [InlineKeyboardButton(text='Частотный криптоанализ 📊', callback_data='cryptoanalysis')],
          [InlineKeyboardButton(text='Настройки ⚙️', callback_data = 'settings')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=f)
def settings_inline():
    f = [[InlineKeyboardButton(text='🔒 Шифр', callback_data = 'encrypt')],
         [InlineKeyboardButton(text='💬 Ввод', callback_data='msg')],
         [InlineKeyboardButton(text='🗝 Ключ',callback_data='key')],
         [InlineKeyboardButton(text='🐅 Параметры гаммирования',callback_data='gamma_settings')],
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
         [InlineKeyboardButton(text='🔭 Гаммирование', callback_data='xor_cipher')],
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
        [InlineKeyboardButton(text='🔙 Назад', callback_data='back')],
        [InlineKeyboardButton(text='🔄 Замена символов в тексте', callback_data='change')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)
def gamma_inline_settings():
    inline_kb_list = [
        [InlineKeyboardButton(text='🌿 Зерно', callback_data='seed')],
        [InlineKeyboardButton(text='🌿 Множитель', callback_data='multiplier')],
        [InlineKeyboardButton(text='🌿 Слагаемое', callback_data='summand')],
        [InlineKeyboardButton(text='🌿 Модуль', callback_data='modulo')],
        [InlineKeyboardButton(text='🔙 Назад', callback_data='back')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)