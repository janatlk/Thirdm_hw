import aioschedule
import asyncio
from aiogram import types, Dispatcher
from config import bot

async def get_id(message:types.Message):
    global chatid
    chatid = message.from_user.id
    await bot.send_message(chat_id=chatid,text="ID получен!")

async def alarm():
    await bot.send_message("Пора на GeekTech!")

async def scheduler():
    aioschedule.every().tuesday.at("17:50").do(alarm)
    aioschedule.every().friday.at("17:50").do(alarm)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)

def register_alarm(dp: Dispatcher):
    dp.register_message_handler(get_id, lambda word: "geektech" in word.text)