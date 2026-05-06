from telebot.types import CallbackQuery
from loader import bot
from keyboards.inline import get_tariff_nav_keyboard

TARIFF_TEXT = (
    "🧩 КОМПЛЕКТАЦИЯ\n\n"
    "📋 СОСТАВ УСЛУГИ\n"
    "1. Подбор материалов\n"
    "- Отделочные материалы\n"
    "- Мебель\n"
    "- Освещение\n"
    "- Электрооборудование\n\n"
    "2. Спецификации\n"
    "- Спецификации материалов к проекту с артикулами и количеством\n\n"
    "💰 СТОИМОСТЬ\n"
    "20 000 руб. — площадь до 50 кв.м.\n"
    "400 руб./кв.м. — площадь более 50 кв.м.\n\n"
    "⏳ ДЛИТЕЛЬНОСТЬ\n"
    "от 7 рабочих дней\n\n"
    "*Данная услуга является дополнительной к дизайн-проекту/редизайну, отдельное приобретение невозможно"
)

@bot.callback_query_handler(func=lambda call: call.data == "tariff_info_complect")
def tariff_info_complect(call: CallbackQuery):
    bot.answer_callback_query(call.id)
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=None
    )
    bot.send_message(
        call.message.chat.id,
        TARIFF_TEXT,
        reply_markup=get_tariff_nav_keyboard(),
        disable_web_page_preview=True
    )