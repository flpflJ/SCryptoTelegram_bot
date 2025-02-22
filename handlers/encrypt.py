from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from keyboards.all_keyboards import greet_kb

encryrouter = Router()

@encryrouter.message(F.text == 'Настройки ⚙️')
async def cmd_start_3(message: Message):
    #calling inline keyboard in answer.look line 11, argument 2.
    await message.answer('потенциальные настройки')

@encryrouter.callback_query(F.data == 'cryptmesg')
async def receive_message_for_encrypt(call: CallbackQuery):
    await call.message.answer() #looks like that i need to receive message, save it, format it and send the answer?