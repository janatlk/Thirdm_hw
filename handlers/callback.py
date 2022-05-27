from config import dp, bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from aiogram import types, Dispatcher


async def quiz2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call2 = InlineKeyboardButton("next", callback_data="button_call2")
    markup.add(button_call2)
    question = "В каком году распался СССР?"
    answers = ['1990', '1993', '1991', '2001']
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question, options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def quiz3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call4 = InlineKeyboardButton("next", callback_data="button_call4")
    markup.add(button_call4)
    question1 = "В каком году ?"
    answers1 = ['да', 'нет', '2000', '20011']
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question1,
        options=answers1,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        # reply_markup=markup
    )


def register_callbacks(dp: Dispatcher):
    dp.register_callback_query_handler(quiz2, lambda call: call.data == "button_call")
    dp.register_callback_query_handler(quiz3, lambda call: call.data == 'button_call2')
