from telebot.types import CallbackQuery
from loader import bot
from states.calc_states import CalcStates
from keyboards.inline import get_calc_waiting_area_keyboard

@bot.callback_query_handler(func=lambda call: call.data == "calc_design")
def calc_design(call: CallbackQuery):
    bot.answer_callback_query(call.id)
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=None
    )
    bot.set_state(call.from_user.id, CalcStates.waiting_area, call.message.chat.id)
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        data["tariff_name"] = "Дизайн-проект"
        data["tariff_code"] = "design"
    sent = bot.send_message(
        call.message.chat.id,
        "Введите площадь жилья или отдельного помещения (в кв.м):",
        reply_markup=get_calc_waiting_area_keyboard()
    )
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        data["prompt_message_id"] = sent.message_id