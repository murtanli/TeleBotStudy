from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from . import config
from aiogram.client.default import DefaultBotProperties

bot = Bot(
        token=config.TELEGRAM_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )
dp = Dispatcher()
