from config import dp, bot
from aiogram import types, Dispatcher
from random import choice
from config import ADMIN


async def echo(message: types.Message):
    x = message.text
    try:
        x = int(x)
        c = 1
    except:
        pass
        c = 0
    if message.text.startswith('game'):
        if message.from_user.id == ADMIN:
            rnd = ['🎲', '🎯', '🎳', '🏀', '⚽', '🎰']
            await bot.send_dice(message.chat.id, emoji=(choice(rnd)))
        else:
            await bot.send_message(message.chat.id, f'Вы не админ')
        c = 3
    elif message.text == 'dice':
        c = 3
        await bot.send_message(message.chat.id, "Моя очередь:")
        a = await bot.send_dice(message.chat.id, emoji='🎲')
        await bot.send_message(message.chat.id, f"Твоя очередь:")
        b = await bot.send_dice(message.chat.id, emoji='🎲')

        if a.dice.value > b.dice.value:
            await bot.send_message(message.chat.id, "Победил бот! лох")
        elif a.dice.value < b.dice.value:
            await bot.send_message(message.chat.id, "Тебе повезло, но бот все равно лучше!")
        elif a.dice.value == b.dice.value:
            await bot.send_message(message.chat.id, "Ничья! но ты все равно неудачник!")
    if c == 1:
        await bot.send_message(message.chat.id, f"{x * x}")
    elif c == 0:
        await bot.send_message(message.chat.id, x)
    else:
        pass


def register_all(dp: Dispatcher):
    dp.register_message_handler(echo)
