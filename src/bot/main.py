import asyncio
import logging

from aiogram.enums import ParseMode

from .config import TELEGRAM_TOKEN, LOGGING_LEVEL
from .loader import dp, bot
from .handlers.main_commands import *

logger = logging.getLogger(__name__)


@dp.message(Command('start'))
async def send_welcome(message: Message):
    logger.info(f"Получено сообщение /start от {message.from_user.id}: {message.text}")
    await message.answer(
        "🎓<b>Добро пожаловать в наш бот по заказу студенческих работ!</b>🎓 \n"
        "\n💬 Здесь вы можете заказать дипломные, курсовые и другие виды учебных работ быстро и просто! \n"
        "\n✨ <b>Как начать:</b>"
        "\n<b>1.</b> Введите команду <code>/reg</code> для регистрации."
        "\nСледуйте инструкциям бота, чтобы оформить заказ. \n"
        "\n🛠 <b>Наши услуги:</b>"
        "\n- Дипломные работы"
        "\n- Курсовые работы"
        "\n- Рефераты"
        "\n- Отчеты по практике"
        "\n- И многое другое! \n"
        "\n📚 <b>Почему выбирают нас:</b>"
        "\n- Опытные авторы"
        "\n- Индивидуальный подход"
        "\n- Гарантия качества"
        "\n- Своевременное выполнение"
        "\nЕсли у вас возникнут вопросы, не стесняйтесь обращаться к нашей поддержке! \n"
        "\n🎉 <b>Желаем успехов в учебе и приятного сотрудничества!</b>",
        parse_mode=ParseMode.HTML)


@dp.message()
async def empty_message(message: Message):
    await message.answer("Неизвестное сообщение")
async def main():
    logging.basicConfig(
        level=getattr(logging, LOGGING_LEVEL),
    )
    logger.info("Starting the server...")
    logger.info("Запуск бота....")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
