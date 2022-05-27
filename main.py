from config import dp
from aiogram.utils import executor
import logging
from handlers import extra, callback, client, admin, FSM, schedule
from database import bot_db
# from repo import ефыл
import asyncio

async def on_startup(_):
    # asyncio.create_task(ефыл.schedular())
    bot_db.sql_create()

# ефыл.reg(dp)
callback.register_callbacks(dp)
admin.register_pin(dp)
client.register_handler(dp)
FSM.reg_load(dp)
schedule.register_alarm(dp)
extra.register_all(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True,on_startup=on_startup)
