from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from HomeworkGit.parserhw import movies
from HomeworkGit.config import bot,dp


async def start(message: types.Message):
    await bot.send_message(message.chat.id, """
    Вас приветствует бот!
    Возможности клиента:
    /quiz    -     Отправляет мини викторину из 3х вопросов.
    /mem     -     Отправляет вам мемчик.
    /members -     Указывает количество участников в группе.
    /reg     -     Регистрация
    /ch      -     Проверка данных регистрации
    Возможности Админа:
    !pin     -     Закрепляет сообщение на которое вы ответили данной командой.
    !unpin   -     Открепляет все сообщения.
    !admins  -     Отправляет контакты админов.
    !defaultp-     Устанавливает стандартный аватар чата.
    Пока это все!
    """)


async def quiz1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call = InlineKeyboardButton("next", callback_data="button_call")
    markup.add(button_call)

    question = "Владелец какой компании является Марк Цекерберг?"
    answers = ["VK", "FaceBook", "YouTube", "Telegram"]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup)


photo = open(f"photos/unnamed.jpg", "rb")


async def mem(message: types.Message):
    await bot.send_photo(message.chat.id, photo=photo)
    # await bot.send_message(message.chat.id,'photo')

async def parser_(message: types.Message):
    data = movies.parser()
    for i in data:
        await bot.send_message(message.chat.id,f"{i['title']}\n\n{i['desc']})\n{i['link']}")


async def pin(message: types.Message):
    await bot.pin_chat_message(message.reply_to_message.from_user)
async def countmembers(message: types.Message):
    await bot.send_message(message.chat.id,f"Количество участников чата - {await bot.get_chat_members_count(message.chat.id)}")

def register_handler(dp: Dispatcher):
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(parser_,commands=['news'])
    dp.register_message_handler(quiz1, commands=['quiz'])
    dp.register_message_handler(pin, commands=['pin'])
    dp.register_message_handler(countmembers, commands=['members'], commands_prefix="!/")
    dp.register_message_handler(start, commands=['start', 'intro', 'help', 'instruction'])
