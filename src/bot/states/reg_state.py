from aiogram.filters.state import State, StatesGroup

class RegState(StatesGroup):
    fio = State()
    group_number = State()
    special_study = State()
    currect_info = State()