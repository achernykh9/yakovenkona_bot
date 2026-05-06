from telebot.types import CallbackQuery
from loader import bot
from keyboards.inline import get_calc_menu
from database import save_event


@bot.callback_query_handler(func=lambda call: call.data == "calc_services_menu")
def calc_services_menu(call: CallbackQuery):
    bot.answer_callback_query(call.id)
    save_event(call.from_user, call.message.chat.id, "calc_services_menu")
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=None
    )
    bot.send_message(
        call.message.chat.id,
        "Выберите тариф для расчета стоимости:",
        reply_markup=get_calc_menu()
    )