from telebot.types import CallbackQuery
from loader import bot
from keyboards.inline import get_calc_menu

@bot.callback_query_handler(func=lambda call: call.data == "calc_back")
def calc_back(call: CallbackQuery):
    bot.answer_callback_query(call.id)
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=None
    )
    bot.delete_state(call.from_user.id, call.message.chat.id)
    bot.send_message(
        call.message.chat.id,
        "Выберите тариф для расчета стоимости:",
        reply_markup=get_calc_menu()
    )