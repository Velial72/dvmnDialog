from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from environs import Env

from dialog import detect_intent_text

env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Zzz...')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


@dp.message()
async def send_answer(message: Message):
    serialized_answer = detect_intent_text('dvmn-bot-ynkq', message.from_user.id, message.text, flag=False)
    if serialized_answer is not None:
        await bot.send_message(chat_id=message.chat.id, text=serialized_answer['answer'])


if __name__ == '__main__':
    dp.run_polling(bot)