from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from ..loader import dp

from ..states import RegState


async def start_registration(message: Message, state: FSMContext):
    await message.answer("Введите ваше ФИО:")
    await state.set_state(RegState.fio)

@dp.message(RegState.fio)
async def enter_group_number(message: Message, state: FSMContext):
    await state.update_data(fio=message.text)
    await message.answer("Введите номер группы")
    await state.set_state(RegState.group_number)

@dp.message(RegState.group_number)
async def enter_special(message: Message, state: FSMContext):
    await state.update_data(group_number=message.text)
    await message.answer("Введите название специальности")
    await state.set_state(RegState.special_study)


@dp.message(RegState.special_study)
async def process_fio(message: Message, state: FSMContext):
    await state.update_data(special_study=message.text)
    data = await state.get_data()
    await message.answer(f"<b>Спасибо, проверьте введенную информацию ! Она будет находится во всех работах !<b>\n"
                         f"<b>Фио:</b> {data["fio"]}\n"
                         f"<b>Группа:</b> {data["group_number"]}\n"
                         f"<b>Название специальности:</b> {data["special_study"]}\n"
                         f"<b>Сохранено!</b>")
    #СДЕЛАТЬ СОХРАНЕНИЕ В БД
    await state.clear()
