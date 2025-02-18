from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from keyboards.all_keyboards import greet_kb

encryrouter = Router()

@encryrouter.message(F.text == 'Настройки ⚙️')
async def cmd_start_3(message: Message):
    await message.answer('потенциальные настройки')