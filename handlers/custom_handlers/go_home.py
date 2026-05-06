from telebot.types import CallbackQuery
from loader import bot
from keyboards.inline import get_start_menu

@bot.callback_query_handler(func=lambda call: call.data == "go_home")
def go_home(call: CallbackQuery):
    name = call.from_user.first_name or "пользователь"
    text = (
        f"Привет, {name}! Я - чат-бот, который поможет Вам:\n"
        "1. Ознакомиться с тарифами услуг.\n"
        "2. Подобрать услуги по дизайну интерьера и рассчитать стоимость проекта."
    )
    bot.answer_callback_query(call.id)
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=None
    )
    bot.send_message(call.message.chat.id, text, reply_markup=get_start_menu())