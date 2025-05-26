from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
def inline_greet():
    f = [[InlineKeyboardButton(text='Зашифровать 🔑', callback_data = 'encrypto')],
          [InlineKeyboardButton(text='Расшифровать 🔐', callback_data = 'decrypt')],
         [InlineKeyboardButton(text='Частотный криптоанализ 📊', callback_data='cryptoanalysis')],
         [InlineKeyboardButton(text='Электронная подпись',callback_data='sign')],
         [InlineKeyboardButton(text='Протокол обмена Диффи-Хеллмана', callback_data='call_diffie')],
          [InlineKeyboardButton(text='Настройки ⚙️', callback_data = 'settings')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=f)

def settings_inline():
    f = [[InlineKeyboardButton(text='🔒 Шифр', callback_data = 'encrypt')],
         [InlineKeyboardButton(text='💬 Ввод', callback_data='msg')],
         [InlineKeyboardButton(text='🗝 Ключ',callback_data='key')],
         [InlineKeyboardButton(text='🐅 Параметры гаммирования',callback_data='gamma_settings')],
         [InlineKeyboardButton(text='Параметры RSA',callback_data='rsa_settings')],
         [InlineKeyboardButton(text='Параметры протокола Диффи-Хеллмана',callback_data='diffie_settings')],
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
         [InlineKeyboardButton(text='DES',callback_data='DES')],
         [InlineKeyboardButton(text='RSA',callback_data='rsa')],
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

def crypto_inline_signature():
    inline_kb_list = [
        [InlineKeyboardButton(text='Подписать', callback_data='sign_message')],
        [InlineKeyboardButton(text='Проверить подпись', callback_data='verify_message')],
        [InlineKeyboardButton(text='🔙 Назад', callback_data='settings')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

def diffie_hellman_inline_settings():
    inline_kb_list = [
        [InlineKeyboardButton(text='Параметр g', callback_data='seed_g')],
        [InlineKeyboardButton(text='Параметр p', callback_data='seed_p_diffie')],
        [InlineKeyboardButton(text='🔙 Назад', callback_data='settings')]
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

def rsa_inline_settings():
    inline_kb_list = [
        [InlineKeyboardButton(text='🌿 Простое число p', callback_data='seed_p')],
        [InlineKeyboardButton(text='🌿 Простое число q', callback_data='seed_q')],
        [InlineKeyboardButton(text='Модуль', callback_data='rsa_module')],
        [InlineKeyboardButton(text='Секретная экспонента', callback_data='rsa_d')],
        [InlineKeyboardButton(text='Открытая экспонента',callback_data='seed_e')],
        [InlineKeyboardButton(text='Подпись', callback_data='rsa_sign')],
        [InlineKeyboardButton(text='🔙 Назад', callback_data='back')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)