from telebot.types import CallbackQuery
from loader import bot
from keyboards.inline import get_tariff_nav_keyboard

TARIFF_TEXT = (
    "🛠 ТЕХНИЧЕСКИЙ ПРОЕКТ\n\n"
    "📋 СОСТАВ УСЛУГИ\n"
    "1. Составление технического задания:\n"
    "- Обмер\n"
    "- Анкета\n\n"
    "2. Разработка планировочного решения:\n"
    "- 3D модели каждого варианта, которые вы можете открыть у себя на планшете или телефоне\n\n"
    "3. Разработка планов:\n"
    "- Обмерный план\n"
    "- План демонтажа\n"
    "- План монтажа\n"
    "- План расстановки мебели\n"
    "- План расстановки мебели с размерами\n"
    "- Схема отделки стен\n"
    "- План привязки сантехнического оборудования\n"
    "- Схема раскладки напольных покрытий\n"
    "- Схема теплых полов и привязки отопительных приборов\n"
    "- План потолков\n"
    "- Схема привязки осветительного оборудования\n"
    "- Схема групп включения и привязки выключателей\n"
    "- Схема привязки розеток и электровыводов\n"
    "- Спецификация отделочных материалов\n"
    "- Спецификация мебели и сантехнического оборудования\n"
    "- Спецификация осветительного оборудования\n"
    "- Спецификация электрооборудования\n"
    "- Белая 3D модель\n\n"
    "💰 СТОИМОСТЬ\n"
    "80 000 руб. — площадь до 50 кв.м.\n"
    "1600 руб./кв.м. — площадь более 50 кв.м.\n\n"
    "⏳ ДЛИТЕЛЬНОСТЬ\n"
    "от 20 рабочих дней\n\n"
    "🔗 <a href='https://www.behance.net/gallery/243313205/tehnicheskij-proekt-kvartiry-445-kvm'>ПОСМОТРЕТЬ ПРИМЕР ПРОЕКТА</a>"
)

@bot.callback_query_handler(func=lambda call: call.data == "tariff_info_technical")
def tariff_info_technical(call: CallbackQuery):
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