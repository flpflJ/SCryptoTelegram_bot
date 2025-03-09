import asyncio
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from create_bot import bot
from aiogram.fsm.context import FSMContext
from aiogram.utils.chat_action import ChatActionSender
from handlers.start import message_to_crypto
from keyboards.all_keyboards import settings_encrypt_inline, crypto_inline_greet, inline_greet, settings_inline
from utils.my_utils import atbashcrypt, caesarcrypt, richelieu

encryrouter = Router()

ddd = []
kkk = []
MESSAGE_MAX_LENGTH = 4096

@encryrouter.callback_query(F.data.in_(['atbash', 'caesar', 'richeliu']))
async def cypherReceive(call: CallbackQuery, state: FSMContext):
    async with ChatActionSender(bot=bot, chat_id=call.from_user.id):
        await call.message.edit_text('Шифр успешно выбран. Выберите опцию', reply_markup=settings_inline())
    await state.update_data(typeOfCrypt=call.data)

@encryrouter.callback_query(F.data == 'msg')
async def msgReceiveCallback(call: CallbackQuery, state: FSMContext):
    async with ChatActionSender(bot=bot, chat_id = call.from_user.id):
        await call.message.answer('Введите сообщение:')
    await state.set_state(message_to_crypto.messagerec)

@encryrouter.message(F.text, message_to_crypto.messagerec)
async def cmd_message_receive(message: Message, state: FSMContext):
    text = message.text
    ddd.append(text)
    await state.update_data(messagerec=''.join(ddd))
    if(len(ddd) == 1):
        await message.answer(f'<b>Сообщение введено</b>. Выберите опцию', reply_markup=settings_inline())
    async with ChatActionSender(bot=bot, chat_id=message.chat.id):
        await asyncio.sleep(1)
    ddd.clear()
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
        await asyncio.sleep(1)
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
    if(data.get("typeOfCrypt") is None):
        await call.message.edit_text('<b>Не задан алгоритм шифрования.</b>',reply_markup=inline_greet())
    elif(data.get("messagerec") is None or encrypted_message == ''):
        await call.message.edit_text('<b>Не введено сообщение.</b>', reply_markup=inline_greet())
    elif((cypher == 'richeliu' or cypher == 'caesar') and data.get("key") is None):
        await call.message.edit_text('<b>Не задан ключ.</b>', reply_markup=inline_greet())
    else:
        if len(encrypted_message) <= MESSAGE_MAX_LENGTH:
            await call.message.answer(f'<tg-spoiler>{encrypted_message}</tg-spoiler>')
            await call.message.answer('Сообщение обработано. ', reply_markup=crypto_inline_greet())
        else:
            for x in range(0,len(encrypted_message), MESSAGE_MAX_LENGTH):
                msg = encrypted_message[x: x + MESSAGE_MAX_LENGTH]
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
    if(data.get("typeOfCrypt") is None):
        await call.message.edit_text('<b>Не задан алгоритм шифрования.</b>',reply_markup=inline_greet())
    elif(data.get("messagerec") is None or encrypted_message == ''):
        await call.message.edit_text('<b>Не введено сообщение.</b>', reply_markup=inline_greet())
    elif((cypher == 'richeliu' or cypher == 'caesar') and data.get("key") is None):
        await call.message.edit_text('<b>Не задан ключ.</b>', reply_markup=inline_greet())
    else:
        if len(encrypted_message) <= MESSAGE_MAX_LENGTH:
            await call.message.answer(f'<tg-spoiler>{encrypted_message}</tg-spoiler>')
            await call.message.answer('Сообщение обработано. ', reply_markup=crypto_inline_greet())
        else:
            for x in range(0, len(encrypted_message), MESSAGE_MAX_LENGTH):
                msg = encrypted_message[x: x + MESSAGE_MAX_LENGTH]
                await call.message.answer(f'<tg-spoiler>{msg}</tg-spoiler>')
            await call.message.answer('Сообщение обработано. ', reply_markup=crypto_inline_greet())
    await state.set_state()
