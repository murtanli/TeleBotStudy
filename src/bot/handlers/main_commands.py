from aiogram import F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from .registration import start_registration

from ..utils.var import hello
from ..loader import dp


@dp.message(F.text.in_(hello))
async def hi_message(message: Message):
    await message.answer("Привет !")


@dp.message(Command('reg'))
async def handle_registration(message: Message, state: FSMContext):
    await start_registration(message, state)
