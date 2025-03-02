from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from create_bot import bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.chat_action import ChatActionSender
from keyboards.all_keyboards import inline_greet, crypto_inline_greet, settings_inline, settings_encrypt_inline

start_router = Router()

class message_to_crypto(StatesGroup):
    typeOfCrypt = State()
    messagerec = State()
    key = State()
@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать. Выберите опцию',reply_markup=inline_greet())
@start_router.callback_query(F.data == 'back')
async def menu(call: CallbackQuery):
    await call.answer()
    async with ChatActionSender(bot=bot, chat_id=call.from_user.id):
        await call.message.delete()
    await call.message.answer('Добро пожаловать. Выберите опцию',reply_markup=inline_greet())
@start_router.callback_query(F.data == 'settings')
async def menu(call: CallbackQuery):
    await call.answer()
    async with ChatActionSender(bot=bot, chat_id=call.from_user.id):
        await call.message.delete()
    await call.message.answer('Настройки: ',reply_markup=settings_inline())

@start_router.callback_query(F.data == 'encrypt')
async def menu(call: CallbackQuery, state: FSMContext):
    await call.answer()
    async with ChatActionSender(bot=bot, chat_id=call.from_user.id):
        await call.message.delete()
    await call.message.answer('Выбор',reply_markup=settings_encrypt_inline())
    await state.set_state(message_to_crypto.messagerec)

#@start_router.message(F.text == 'Зашифровать 🔑') #possible settings
#async def cmd_crypto_start(message: Message):
    #calling inline keyboard in answer. look line 11, argument 2.
    #await message.reply('Выберите шифр', reply_markup=encrypt)