from aiogram import Router, F
from create_bot import bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.chat_action import ChatActionSender
from keyboards.all_keyboards import greet_kb, encrypt, crypto_inline_greet

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать. Выберите опцию',reply_markup=greet_kb)
@start_router.callback_query(F.data == 'back')
async def menu(call: CallbackQuery):
    await call.answer()
    async with ChatActionSender(bot=bot, chat_id=call.from_user.id):
        await call.message.delete()
    await call.message.answer('Добро пожаловать. Выберите опцию',reply_markup=greet_kb)

@start_router.message(F.text == 'Зашифровать 🔑') #possible settings
async def cmd_crypto_start(message: Message):
    #calling inline keyboard in answer. look line 11, argument 2.
    await message.reply('Выберите шифр', reply_markup=encrypt)