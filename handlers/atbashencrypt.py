import asyncio
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from create_bot import bot
from aiogram.fsm.context import FSMContext
from aiogram.utils.chat_action import ChatActionSender

from handlers.start import message_to_crypto
from keyboards.all_keyboards import settings_encrypt_inline, crypto_inline_greet, inline_greet, settings_inline
from utils.my_utils import atbashcrypt, caesarcrypt, richelieu

encryrouter = Router()

@encryrouter.callback_query(F.data.in_(['atbash', 'caesar', 'richeliu']))
async def cypherReceive(call: CallbackQuery, state: FSMContext):
    async with ChatActionSender(bot=bot, chat_id=call.from_user.id):
        #await call.message.answer('Введите сообщение: ')
        await call.message.delete()
        await call.message.answer('Шифр успешно выбран!', reply_markup=settings_inline())
    await state.update_data(typeOfCrypt=call.data)

@encryrouter.callback_query(F.data == 'msg')
async def msgReceive(call: CallbackQuery, state: FSMContext):
    async with ChatActionSender(bot=bot, chat_id = call.from_user.id):
        await asyncio.sleep(1)
        await call.message.delete()
        await call.message.answer('Введите сообщение:')
    await state.set_state(message_to_crypto.messagerec)

@encryrouter.message(F.text, message_to_crypto.messagerec)
async def cmd_atbash_process(message: Message, state: FSMContext):
    await state.update_data(messagerec=message.text)
    #encrypted_message = atbashcrypt(message.text)
    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        await asyncio.sleep(1)
        #encrypted_message = atbashcrypt(message.text)
    await message.answer(f'<b>Сообщение введено</b>. Выберите опцию', reply_markup=settings_inline())
    #await message.answer(f'<tg-spoiler>{encrypted_message}</tg-spoiler>')
    #await state.clear()

@encryrouter.callback_query(F.data == 'key')
async def keyReceive(call: CallbackQuery, state: FSMContext):
    async with ChatActionSender(bot=bot, chat_id=call.from_user.id):
        await asyncio.sleep(1)
        await call.message.delete()
        await call.message.answer('Введите ключ. Формат ключа: текст, число, либо (x,y,z,...).., где x,y,z - числа. Например (3,2,1)(2,1)')
    await state.set_state(message_to_crypto.key)

@encryrouter.message(F.text, message_to_crypto.key)
async def cmd_atbash_process(message: Message, state: FSMContext):
    await state.update_data(key=message.text)
    #encrypted_message = atbashcrypt(message.text)
    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        await asyncio.sleep(1)
        #encrypted_message = atbashcrypt(message.text)
    await message.answer(f'<b>Ключ введен</b>. Выберите опцию', reply_markup=settings_inline())
    #await message.answer(f'<tg-spoiler>{encrypted_message}</tg-spoiler>')
    #await state.clear()
@encryrouter.callback_query(F.data == 'encrypto')
async def encryptCmd(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    async with ChatActionSender.typing(bot=bot, chat_id=call.from_user.id):
        await call.message.delete()
        await asyncio.sleep(1)
        cypher = data.get("typeOfCrypt")
        encrypted_message = ''
        if(cypher == 'atbash'):
            encrypted_message = atbashcrypt(data.get("messagerec"))
        elif(cypher == 'caesar'):
            encrypted_message = caesarcrypt(data.get("messagerec"),data.get("key"),0)
        elif(cypher == 'richeliu'):
            encrypted_message = richelieu(data.get("messagerec"),data.get("key"),0)
    if(encrypted_message == ''):
        await call.message.answer('<b>Не введено сообщение.</b>', reply_markup=inline_greet())
    elif(type(data.get("typeOfCrypt")) == ''):
        await call.message.answer('<b>Не задан алгоритм шифрования.</b>',reply_markup=inline_greet())
    elif((cypher == 'richeliu' or cypher == 'caesar') and type(data.get("key"))==''):
        await call.message.answer('<b>Не задан ключ.</b>', reply_markup=inline_greet())
    else:
        await call.message.answer(f'<tg-spoiler>{encrypted_message}</tg-spoiler>', reply_markup=crypto_inline_greet())
    await state.clear()
@encryrouter.callback_query(F.data == 'decrypt')
async def encryptCmd(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    async with ChatActionSender.typing(bot=bot, chat_id=call.from_user.id):
        await call.message.delete()
        await asyncio.sleep(1)
        cypher = data.get("typeOfCrypt")
        encrypted_message = ''
        if(cypher == 'atbash'):
            encrypted_message = atbashcrypt(data.get("messagerec"))
        elif(cypher == 'caesar'):
            encrypted_message = caesarcrypt(data.get("messagerec"),data.get("key"),1)
        elif(cypher == 'richeliu'):
            encrypted_message = richelieu(data.get("messagerec"),data.get("key"),1)
    if(encrypted_message == ''):
        await call.message.answer('<b>Не введено сообщение.</b>', reply_markup=inline_greet())
    elif(data.get("typeOfCrypt") is None):
        await call.message.answer('<b>Не задан алгоритм шифрования.</b>',reply_markup=inline_greet())
    elif((cypher == 'richeliu' or cypher == 'caesar' or cypher==None) and data.get("key") is None):
        await call.message.answer('<b>Не задан ключ.</b>', reply_markup=inline_greet())
    else:
        await call.message.answer('Зашифрованное сообщение: ', reply_markup=crypto_inline_greet())
    #await call.message.answer(f'<tg-spoiler>{encrypted_message}</tg-spoiler>', reply_markup=crypto_inline_greet())
    await state.clear()
