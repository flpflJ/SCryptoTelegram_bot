import asyncio
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from keyboards.all_keyboards import greet_kb
from keyboards.all_keyboards import encrypt
from create_bot import bot
from aiogram.fsm.context import FSMContext
from aiogram.utils.chat_action import ChatActionSender
from utils.my_utils import atbashcrypt
class message_to_crypto_atbash(StatesGroup):
    messagerec = State()

encryrouter = Router()

@encryrouter.message(F.text == 'Зашифровать 🔑') #possible settings
async def cmd_crypto_start(message: Message):
    #calling inline keyboard in answer. look line 11, argument 2.
    await message.reply('Выберите шифр', reply_markup=encrypt)
@encryrouter.message(F.text == 'Шифр Атбаш')
async def cmd_atbash_receiveMessage(message: Message, state: FSMContext):
    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        await asyncio.sleep(2)
        await message.answer('Введите сообщение: ')
    await state.set_state(message_to_crypto_atbash.messagerec)
@encryrouter.message(F.text, message_to_crypto_atbash.messagerec)
async def cmd_atbash_process(message: Message, state: FSMContext):
    await state.update_data(messagerec=message.text)
    encrypted_message = atbashcrypt(message.text)
    async with ChatActionSender.typing(bot=bot, chat_id=message.chat.id):
        await asyncio.sleep(3)
        encrypted_message = atbashcrypt(message.text)
    await message.answer(f'Зашифрованное сообщение: \n'f'<tg-spoiler>{encrypted_message}</tg-spoiler>')

@encryrouter.message(F.text == 'Шифр Цезаря')
async def cmd_caesar_receiveMessage(message: Message):
    await message.reply('Введите сообщение')
@encryrouter.message(F.text == 'Шифр Ришелье')
async def cmd_richelieu_receiveMessage(message: Message):
    await message.reply('Введите сообщение')
#@encryrouter.callback_query(F.data == 'cryptmesg')
#async def receive_message_for_encrypt(call: CallbackQuery):
#    await call.message.answer() #looks like that i need to receive message, save it, format it and send the answer?
### IN FUTURE