from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from Database import make_db, edit_profile

API_TOKEN = '5970034605:AAHC81Ssc8ZRQdyVieWWV0NNLcCFz4FC6wQ'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

HELP_MENU = """
/help - помощь
/keyboard - клавиатура"""

kb = ReplyKeyboardMarkup()
kb.add(KeyboardButton("$"))
kb.add(KeyboardButton("€"))


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    user_id = str(message.from_user.id)
    make_db()
    edit_profile(user_id=user_id)
    #хранение айди в памяти бота
    spisok_id = []
    if user_id not in spisok_id:
        spisok_id.append(user_id)

    await message.reply(text=HELP_MENU)


@dp.message_handler(commands=['keyboard'])
async def send_keyboard(message: types.Message):
    # await bot.delete_message(message.from_user.id, message_id=message.message_id) #delete message from user
    await bot.send_message(message.from_user.id, text='Выбери валюту', reply_markup=kb)


@dp.message_handler()
async def send_value(message: types.Message):
    if message.text == "$":
        await bot.send_message(message.from_user.id, text='70.04')

    elif message.text == "€":
        await bot.send_message(message.from_user.id, text='76.96')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
