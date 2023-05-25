"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types

from googletrans import Translator
translator = Translator()

API_TOKEN = '6087007134:AAGLJyDwhxOMdrNW5gI24wVjWDev1fvxrO0'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.answer("Hello, I'm Translater bot 🤖.\nThis bot translates into Uzbek, Russian, English and Chinese languages.")



@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.answer("Sizga qanday yordam bera olaman 🤔?.")



@dp.message_handler()
async def echo(message: types.Message):
    translator = Translator()
    savol = message.text
    try:
        Uzbek = translator.translate(savol, dest = "uz")
        javob = Uzbek.text
        await message.answer(javob)
    except:
        await message.answer('This word was not found')
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)