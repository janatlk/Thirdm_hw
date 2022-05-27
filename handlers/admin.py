from aiogram import types, Dispatcher

from config import bot, ADMIN, photods


async def pin(message: types.Message):
    if message.from_user.id not in ADMIN:
        await message.reply("Вы не являетесь админоm в данной группе!")
    elif message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await bot.send_message(message.chat.id, 'Нужно ответить на сообщение чтобы его закрепить!')


async def unpin(message: types.Message):
    if message.from_user.id not in ADMIN:
        await message.reply("Для использования этой команды вы олжны быть Админом!")
    else:
        await bot.unpin_all_chat_messages(message.chat.id)

async def kick(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMIN:
            await message.reply("Вы не являетесь админом в данной группе!")
        if message.reply_to_message:
            await bot.kick_chat_member(message.chat.id,message.reply_to_message.from_user.id)
        else:
            await message.reply("Ответьте на сообщение чтобы кикнуть!")
    else:
        await message.reply("Используйте команду в группе!")

async def get_administrators(message:types.Message):
    a = ''
    if message.chat.type != 'private':
        if message.from_user.id not in ADMIN:
            await message.reply("Вы не являетесь админом в данной группе!")
        else:
            chat_admins = await message.chat.get_administrators()
            for i in chat_admins:
                for l in i:
                    for k in l:
                        try:
                            k['username'] = k['username']
                            a += '@'
                            a += k['username']
                            a += ','
                        except:
                            pass
        try:
            a = list(a)
            a.pop(-1)
            a.append('.')
            m = ''.join(a)
            await bot.send_message(message.chat.id, f"{m}")
        except:
            pass
    else:
        await message.reply("Данная команда не работает в личных сообщениях!")
# class FSMAdmin(StatesGroup):
#     picture = State()
#
# async def chat_photo(message:types.Message,state: FSMContext):
#     if message.chat.type != 'private':
#         if message.from_user.id in ADMIN:
#             await FSMAdmin.picture.set()
#             await bot.send_message(message.chat.id,"""
#             Ожидаю фото...
#
#             """)
# async def load_photo(message:types.Message,state: FSMContext):
#     async with state.proxy() as data:
#         data["picture"] = message.photo[0].file_id
#     await FSMAdmin.next()
#     await state.finish()
#     q = data['picture']
#     await bot.send_photo(message.chat.id,photo=data['picture'])
#     print(data)
#     await bot.set_chat_photo(message.chat.id, data['picture'])
async def chat_photo(message:types.Message):
    if message.chat.type != 'private':
        if message.from_user.id in ADMIN:
            await bot.set_chat_photo(message.chat.id,photods)
        else:
            await message.reply("Вы не являетесь админом")
    else:
        await message.reply("В личных не работает")
def register_pin(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix="!/")
    dp.register_message_handler(unpin, commands=['unpin'], commands_prefix="!/")
    dp.register_message_handler(kick,commands=['kick'],commands_prefix="!/")
    dp.register_message_handler(chat_photo,commands='defaultp',commands_prefix = '!/')
    dp.register_message_handler(get_administrators,commands='admins',commands_prefix='!/')