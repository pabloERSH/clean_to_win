import asyncio
import logging
import sys
import webbrowser

from decouple import config

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = config('TOKEN')

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Открыть приложение',
                    #web_app=WebAppInfo(url=f'https://www.figma.com/proto/YBXDlyrBJPT3TADkyw0bBE/Clen-to-win?node-id=212-1843&node-type=canvas&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=212%3A1843')
                    web_app=WebAppInfo(url=f'http://127.0.0.1:8000/app/main_page/')
                )
            ]
        ]
    )
    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}!\n"
                         f"Для запуска приложения нажмите на кнопку ниже!", reply_markup=markup)


@dp.message(Command('site'))
async def site(message: Message):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Перейти на сайт',
                    url=f'http://127.0.0.1:8000/'
                )
            ]
        ]
    )
    await message.answer(f"Ссылка на наш сайт с информацией о проекте", reply_markup=markup)


@dp.message(Command('help'))
async def command_help_handler(message: Message) -> None:
    await message.answer("Команды:\n/start - открыть приложение\n/site - перейти на наш сайт с информацией о проекте")


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Команды:\n/start - открыть приложение\n/site - перейти на наш сайт с информацией о проекте")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())