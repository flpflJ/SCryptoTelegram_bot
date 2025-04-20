import asyncio
import base64

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto, BufferedInputFile
from create_bot import bot
from aiogram.fsm.context import FSMContext
from aiogram.utils.chat_action import ChatActionSender
from handlers.start import message_to_crypto
from keyboards.all_keyboards import settings_encrypt_inline, crypto_inline_greet, inline_greet, settings_inline, \
    crypto_inline_change_text_params
from utils.my_utils import atbashcrypt, caesarcrypt, richelieu, gronsfeld_cipher, vigenere_cipher, playfair_cipher, \
    symbol_count, generate_hist, ind_of_c, replace_symbol, parse_validate_pairs, swap_symbol, check_alphabets

encryrouter = Router()

ddd = []
kkk = []
MESSAGE_MAX_LENGTH = 4096

@encryrouter.callback_query(F.data.in_(['atbash', 'caesar', 'richeliu', 'gronsfeld', 'vigenere', 'playfair']))
async def cypherReceive(call: CallbackQuery, state: FSMContext):
    async with ChatActionSender(bot=bot, chat_id=call.from_user.id):
        await call.message.edit_text('Шифр успешно выбран. Выберите опцию', reply_markup=settings_inline())
    await state.update_data(typeOfCrypt=call.data)

@encryrouter.callback_query(F.data == 'msg')
async def msgReceiveCallback(call: CallbackQuery, state: FSMContext):
    async with ChatActionSender(bot=bot, chat_id = call.from_user.id):
        await call.message.answer('Введите сообщение, либо отправьте файл:')
    await state.set_state(message_to_crypto.messagerec)

@encryrouter.message(F.content_type.in_({'text', 'sticker', 'document', 'photo', 'video', 'audio', 'voice'}), message_to_crypto.messagerec)
async def cmd_message_receive(message: Message, state: FSMContext):
    file = None
    if message.document:
        file = message.document
    elif message.photo:
        file = message.photo[-1]  # Берем фото в лучшем качестве
    elif message.video:
        file = message.video
    elif message.audio:
        file = message.audio
    elif message.voice:
        file = message.voice
    elif message.sticker:
        file = message.sticker
    text = message.text
    if text:
        ddd.append(text)
        await state.update_data(messagerec=''.join(ddd))
        await state.update_data(isFile=0)
        if(len(ddd) == 1):
            await message.answer(f'<b>Сообщение введено</b>. Выберите опцию', reply_markup=settings_inline())
        #async with ChatActionSender(bot=bot, chat_id=message.chat.id):
            #await asyncio.sleep(1)
        ddd.clear()
        await state.update_data(res_dict=None)
        await state.set_state(state=None)
    if file:
        await state.update_data(isFile=1)
        file_info = await message.bot.get_file(file.file_id)
        downloaded = await message.bot.download_file(file_info.file_path)
        await state.update_data(messagerec=downloaded)
        await message.answer(f'<b>Файл принят</b>. Выберите опцию', reply_markup=settings_inline())
        await state.update_data(res_dict=None)
        await state.set_state(state=None)


@encryrouter.callback_query(F.data == 'key')
async def keyReceive(call: CallbackQuery, state: FSMContext):
    async with ChatActionSender(bot=bot, chat_id=call.from_user.id):
        await call.message.answer('Введите ключ. Формат ключа: текст, число, либо (x,y,z,...).., где x,y,z - числа. Например (3,2,1)(2,1)')
    await state.set_state(message_to_crypto.key)

@encryrouter.message(F.text, message_to_crypto.key)
async def cmd_key_receive(message: Message, state: FSMContext):
    key = message.text
    kkk.append(key)
    await state.update_data(key=''.join(key))
    if(len(kkk) == 1):
        await message.answer(f'<b>Ключ введен</b>. Выберите опцию', reply_markup=settings_inline())
    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        #await asyncio.sleep(1)
        kkk.clear()

@encryrouter.callback_query(F.data == 'encrypto')
async def encryptCmd(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    async with ChatActionSender.typing(bot=bot, chat_id=call.from_user.id):
        cypher = data.get("typeOfCrypt")
        if not(data.get("messagerec") is None):
            if(cypher == 'atbash'):
                encrypted_message = atbashcrypt(data.get("messagerec"))
            elif(cypher == 'caesar'):
                encrypted_message = caesarcrypt(data.get("messagerec"),data.get("key"),0)
            elif(cypher == 'richeliu'):
                encrypted_message = richelieu(data.get("messagerec"),data.get("key"),0)
            elif(cypher == 'gronsfeld'):
                encrypted_message = gronsfeld_cipher(data.get("messagerec"),data.get("key"),0)
            elif(cypher == 'vigenere'):
                encrypted_message = vigenere_cipher(data.get("messagerec"),data.get("key"),0)
            elif(cypher == 'playfair'):
                encrypted_message = playfair_cipher(data.get("messagerec"),data.get("key"),0)
    if(data.get("typeOfCrypt") is None):
        await call.message.edit_text('<b>Не задан алгоритм шифрования.</b>',reply_markup=inline_greet())
    elif(data.get("messagerec") is None or encrypted_message == ''):
        await call.message.edit_text('<b>Не введено сообщение.</b>', reply_markup=inline_greet())
    elif((cypher == 'richeliu' or cypher == 'caesar' or cypher == 'gronsfeld' or cypher == 'vigenere' or cypher == 'playfair') and data.get("key") is None):
        await call.message.edit_text('<b>Не задан ключ.</b>', reply_markup=inline_greet())
    else:
        if len(encrypted_message) <= MESSAGE_MAX_LENGTH:
            if (cypher == 'playfair'):
                await call.message.answer(encrypted_message, parse_mode=None)
            else:
                await call.message.answer(f'<tg-spoiler>{encrypted_message}</tg-spoiler>')
            await call.message.answer('Сообщение обработано. ', reply_markup=crypto_inline_greet())
        else:
            for x in range(0,len(encrypted_message), MESSAGE_MAX_LENGTH):
                msg = encrypted_message[x: x + MESSAGE_MAX_LENGTH]
                if (cypher == 'playfair'):
                    await call.message.answer(msg, parse_mode=None)
                else:
                    await call.message.answer(f'<tg-spoiler>{msg}</tg-spoiler>')
            await call.message.answer('Сообщение обработано. ', reply_markup=crypto_inline_greet())
    await state.set_state()

@encryrouter.callback_query(F.data == 'decrypt')
async def decryptCmd(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    async with ChatActionSender.typing(bot=bot, chat_id=call.from_user.id):
        cypher = data.get("typeOfCrypt")
        if not(data.get("messagerec") is None):
            if(cypher == 'atbash'):
                encrypted_message = atbashcrypt(data.get("messagerec"))
            elif(cypher == 'caesar'):
                encrypted_message = caesarcrypt(data.get("messagerec"),data.get("key"),1)
            elif(cypher == 'richeliu'):
                encrypted_message = richelieu(data.get("messagerec"),data.get("key"),1)
            elif(cypher == 'gronsfeld'):
                encrypted_message = gronsfeld_cipher(data.get("messagerec"),data.get("key"),1)
            elif(cypher == 'vigenere'):
                encrypted_message = vigenere_cipher(data.get("messagerec"),data.get("key"),1)
            elif(cypher == 'playfair'):
                encrypted_message = playfair_cipher(data.get("messagerec"),data.get("key"),1)
    if(data.get("typeOfCrypt") is None):
        await call.message.edit_text('<b>Не задан алгоритм шифрования.</b>',reply_markup=inline_greet())
    elif(data.get("messagerec") is None or encrypted_message == ''):
        await call.message.edit_text('<b>Не введено сообщение.</b>', reply_markup=inline_greet())
    elif((cypher == 'richeliu' or cypher == 'caesar' or cypher == 'gronsfeld' or cypher == 'vigenere' or cypher == 'playfair') and data.get("key") is None):
        await call.message.edit_text('<b>Не задан ключ.</b>', reply_markup=inline_greet())
    else:
        if len(encrypted_message) <= MESSAGE_MAX_LENGTH:
            if (cypher == 'playfair'):
                await call.message.answer(encrypted_message, parse_mode=None)
            else:
                await call.message.answer(f'<tg-spoiler>{encrypted_message}</tg-spoiler>')
            await call.message.answer('Сообщение обработано. ', reply_markup=crypto_inline_greet())
        else:
            for x in range(0, len(encrypted_message), MESSAGE_MAX_LENGTH):
                msg = encrypted_message[x: x + MESSAGE_MAX_LENGTH]
                if (cypher == 'playfair'):
                    await call.message.answer(msg, parse_mode=None)
                else:
                    await call.message.answer(f'<tg-spoiler>{msg}</tg-spoiler>')
            await call.message.answer('Сообщение обработано. ', reply_markup=crypto_inline_greet())
    await state.set_state()

@encryrouter.callback_query(F.data == 'cryptoanalysis')
async def cryptanalysis(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg = data.get("messagerec")
    if (data.get("isFile") is None):
        await call.message.edit_text('<b>Не введено сообщение, либо нет файла.</b>', reply_markup=inline_greet())
    elif(data.get("isFile") == 1):
        try:
            msg = msg.read().decode("utf-8")
            await state.update_data(messagerec=msg)
        except (UnicodeDecodeError, AttributeError):
            await call.message.answer('<b>Проблема с файлом. Вероятно, это не UTF-8?</b>', reply_markup=inline_greet())
            return 0
    try:
        rd,ed,smbcnt = symbol_count(msg)
    except TypeError:
        await call.message.answer('<b>Проблема с сообщением. Вероятно, текст пуст?</b>', reply_markup=inline_greet())
        return 0
    euf,ruf = check_alphabets(msg)
    if data.get("res_dict") is None:
        kd, edd = ind_of_c(msg)
        res_dict = {**kd, **edd}
    else:
        res_dict = data.get("res_dict")
        kd = dict(list(res_dict.items())[:33])
        edd = dict(list(res_dict.items())[33:])

    recvtext = replace_symbol(msg,res_dict)
    if data.get("isFile") == 1:
        await call.message.answer_document(BufferedInputFile(recvtext.encode('utf-8'),filename="out.txt"))
    else:
        if len(recvtext) <= MESSAGE_MAX_LENGTH:
            await call.message.answer(f'<tg-spoiler>{recvtext}</tg-spoiler>')
        else:
            for x in range(0, len(recvtext), MESSAGE_MAX_LENGTH):
                msg = recvtext[x: x + MESSAGE_MAX_LENGTH]
                await call.message.answer(f'<tg-spoiler>{msg}</tg-spoiler>')
    en_hist = generate_hist(ed, 1)
    ru_hist = generate_hist(rd, 0)
    if euf == 1 and ruf == 1:
        photo_1 = InputMediaPhoto(type='photo',media=BufferedInputFile(base64.b64decode(ru_hist),filename="hist_ru.jpg"),caption='Гистограммы')
        photo_2 = InputMediaPhoto(type='photo', media=BufferedInputFile(base64.b64decode(en_hist), filename="hist_en.jpg"))
        media = [photo_1, photo_2]
        await call.message.answer_media_group(media=media)
        await call.message.answer(f'<b>Таблица замены</b>:\n<code>{"\n".join([f"{k} - {v}" for k, v in kd.items()])}</code>')
        await call.message.answer(f'<b>Таблица замены</b>:\n<code>{"\n".join([f"{k} - {v}" for k, v in edd.items()])}</code>',reply_markup=crypto_inline_change_text_params())
    elif euf == 1 and ruf == 0:
        await call.message.answer_photo(BufferedInputFile(base64.b64decode(en_hist),filename="hist_en.jpg"), caption='Гистограмма')
        await call.message.answer(f'<b>Таблица замены</b>:\n<code>{"\n".join([f"{k} - {v}" for k, v in edd.items()])}</code>',reply_markup=crypto_inline_change_text_params())
    elif euf == 0 and ruf == 1:
        await call.message.answer_photo(BufferedInputFile(base64.b64decode(ru_hist),filename="hist_ru.jpg"), caption='Гистограмма')
        await call.message.answer(f'<b>Таблица замены</b>:\n<code>{"\n".join([f"{k} - {v}" for k, v in kd.items()])}</code>',reply_markup=crypto_inline_change_text_params())
    await state.update_data(res_dict=res_dict)
    await state.set_state()

@encryrouter.callback_query(F.data == 'change')
async def table_change(call: CallbackQuery, state: FSMContext):
    async with ChatActionSender(bot=bot, chat_id = call.from_user.id):
        await call.message.answer('Введите символы для замены. Формат для замены символов: А - Б, B - D, ...: ')
    await state.set_state(message_to_crypto.table)

@encryrouter.message(F.text, message_to_crypto.table)
async def table_recv(message: Message, state: FSMContext):
    table_change = message.text
    data = await state.get_data()
    res_dict = data.get("res_dict")
    msg = data.get("messagerec")
    rd,ed,smbcnt = symbol_count(msg)
    left,right = parse_validate_pairs(table_change)
    if left is None:
        await message.answer('Неккоректный ввод. ', reply_markup=crypto_inline_change_text_params())
        await state.set_state()
    else:
        euf, ruf = check_alphabets(msg)
        swap_symbol(left,right, res_dict)
        res_text = replace_symbol(msg,res_dict)
        en_hist = generate_hist(ed, 1)
        ru_hist = generate_hist(rd, 0)
        kd = dict(list(res_dict.items())[:33])
        edd = dict(list(res_dict.items())[33:])
        if data.get("isFile") == 1:
            await message.answer_document(BufferedInputFile(res_text.encode('utf-8'), filename="out.txt"))
        else:
            if len(res_text) <= MESSAGE_MAX_LENGTH:
                await message.answer(f'<tg-spoiler>{res_text}</tg-spoiler>')
            else:
                for x in range(0, len(res_text), MESSAGE_MAX_LENGTH):
                    msg = res_text[x: x + MESSAGE_MAX_LENGTH]
                    await message.answer(f'<tg-spoiler>{msg}</tg-spoiler>')
        if euf == 1 and ruf == 1:
            photo_1 = InputMediaPhoto(type='photo',
                                      media=BufferedInputFile(base64.b64decode(ru_hist), filename="hist_ru.jpg"),
                                      caption='Гистограммы')
            photo_2 = InputMediaPhoto(type='photo',
                                      media=BufferedInputFile(base64.b64decode(en_hist), filename="hist_en.jpg"))
            media = [photo_1, photo_2]
            await message.answer_media_group(media=media)
            await message.answer(
                f'<b>Таблица замены после изменений</b>:\n<code>{"\n".join([f"{k} - {v}" for k, v in kd.items()])}</code>')
            await message.answer(
                f'<b>Таблица замены после изменений</b>:\n<code>{"\n".join([f"{k} - {v}" for k, v in edd.items()])}</code>',
                reply_markup=crypto_inline_change_text_params())
        elif euf == 1 and ruf == 0:
            await message.answer_photo(BufferedInputFile(base64.b64decode(en_hist), filename="hist_en.jpg"),
                                            caption='Гистограмма')
            await message.answer(
                f'<b>Таблица замены после изменений</b>:\n<code>{"\n".join([f"{k} - {v}" for k, v in edd.items()])}</code>',
                reply_markup=crypto_inline_change_text_params())
        elif euf == 0 and ruf == 1:
            await message.answer_photo(BufferedInputFile(base64.b64decode(ru_hist), filename="hist_ru.jpg"),
                                            caption='Гистограмма')
            await message.answer(
                f'<b>Таблица замены после изменений</b>:\n<code>{"\n".join([f"{k} - {v}" for k, v in kd.items()])}</code>',
                reply_markup=crypto_inline_change_text_params())
        await state.update_data(res_dict=res_dict)
        await state.set_state()