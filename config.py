from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from decouple import config

storage = MemoryStorage()

photods = open("photos/unnamed1.jpg",'rb')
Token = config("CODE")
bot = Bot(Token)
dp = Dispatcher(bot=bot,storage=storage)
ADMIN = [5206327279,214214]