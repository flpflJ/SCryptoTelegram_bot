import asyncio
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from keyboards.all_keyboards import greet_kb, encrypt, crypto_inline_greet
from create_bot import bot
from aiogram.fsm.context import FSMContext
from aiogram.utils.chat_action import ChatActionSender
from utils.my_utils import atbashcrypt
class message_to_crypto_atbash(StatesGroup):
    messagerec = State()

caesarrouter = Router()


@caesarrouter.message(F.text == 'Шифр Цезаря')
async def cmd_caesar_receiveMessage(message: Message):
    await message.reply('Введите сообщение')
@caesarrouter.message(F.text, message_to_crypto_atbash.messagerec)
async def cmd_atbash_process(message: Message, state: FSMContext):
    await state.update_data(messagerec=message.text)
    encrypted_message = atbashcrypt(message.text)
    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        await asyncio.sleep(1)
        encrypted_message = atbashcrypt(message.text)
    #await message.answer('Зашифрованное сообщение: ', reply_markup=crypto_inline_greet)
    await message.answer(f'<tg-spoiler>{encrypted_message}</tg-spoiler>')
#@caesarrouter.message(F.text == 'Шифр Ришелье')
#async def cmd_richelieu_receiveMessage(message: Message):
#    await message.reply('Введите сообщение')