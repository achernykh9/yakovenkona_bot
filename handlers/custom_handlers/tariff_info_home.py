from telebot.types import CallbackQuery
from loader import bot
from keyboards.inline import get_tariff_nav_keyboard

TARIFF_TEXT = (
    "🏡 ХОУМСТЕЙДЖИНГ\n\n"
    "📋 СОСТАВ УСЛУГИ\n"
    "1. Составление технического задания:\n"
    "- Обмер\n"
    "- Анкета\n\n"
    "2. Разработка планировочного решения:\n"
    "- 3D модели каждого варианта, которые вы можете открыть у себя на планшете или телефоне\n\n"
    "3. Подбор материалов и мебели на коллажах:\n"
    "- Составление мудборда по проекту\n"
    "- Составление 3D коллажей с подбором материалов и мебели по каждому помещению\n"
    "- Спецификация отделочных материалов\n"
    "- Спецификация мебели и сантехнического оборудования\n"
    "- Спецификация осветительного оборудования\n\n"
    "💰 СТОИМОСТЬ\n"
    "70 000 руб. — площадь до 50 кв.м.\n"
    "1400 руб./кв.м. — площадь более 50 кв.м.\n\n"
    "⏳ ДЛИТЕЛЬНОСТЬ\n"
    "от 20 рабочих дней\n\n"
    "🔗 <a href='https://www.behance.net/gallery/243315317/houmstejdzhing-kvartiry-445-kvm'>ПОСМОТРЕТЬ ПРИМЕР ПРОЕКТА</a>"
)

@bot.callback_query_handler(func=lambda call: call.data == "tariff_info_home")
def tariff_info_home(call: CallbackQuery):
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
        parse_mode="HTML",
        disable_web_page_preview=True
    )