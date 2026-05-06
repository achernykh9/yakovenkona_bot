from telebot.types import CallbackQuery
from loader import bot
from keyboards.inline import get_tariffs_info_keyboard

@bot.callback_query_handler(func=lambda call: call.data == "back_to_tariffs_info")
def back_to_tariffs_info(call: CallbackQuery):
    bot.answer_callback_query(call.id)
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=None
    )
    bot.send_message(
        call.message.chat.id,
        "Отлично! Выберите тариф, о котором хотите узнать:",
        reply_markup=get_tariffs_info_keyboard()
    )