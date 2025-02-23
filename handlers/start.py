from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from keyboards.all_keyboards import greet_kb

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать. Выберите опцию',reply_markup=greet_kb)
