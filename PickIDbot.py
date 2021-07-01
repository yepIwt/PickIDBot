"""
	PickIdBot - tool for receiving the sent type ID
	yepiwt, 2021
"""
import os
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Send whatever you want. An empty message will return your account ID.")

@dp.message_handler(content_types = ["any"])
async def send_id(message: types.Message):
	if message.photo:
		id = message.photo[-1].file_id
	elif message.document:
		id = message.document.file_id
	elif message.voice:
		id = message.voice.file_id
	elif message.audio:
		id = message.audio.file_id
	elif message.sticker:
		id = message.sticker.file_id
	else:
		id = message.from_user.id
	await message.reply(f"```{id}```",parse_mode='Markdown')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
