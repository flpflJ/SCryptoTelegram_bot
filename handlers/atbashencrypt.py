import asyncio
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from create_bot import bot
from aiogram.fsm.context import FSMContext
from aiogram.utils.chat_action import ChatActionSender
from utils.my_utils import atbashcrypt
class message_to_crypto_atbash(StatesGroup):
    messagerec = State()

encryrouter = Router()

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
        await asyncio.sleep(1)
        encrypted_message = atbashcrypt(message.text)
    #await message.answer('Зашифрованное сообщение: ', reply_markup=crypto_inline_greet)
    await message.answer(f'<tg-spoiler>{encrypted_message}</tg-spoiler>')
    await state.clear()
#@encryrouter.callback_query(F.data == 'cryptmesg')
#async def receive_message_for_encrypt(call: CallbackQuery):
#    await call.message.answer() #looks like that i need to receive message, save it, format it and send the answer?
### IN FUTURE