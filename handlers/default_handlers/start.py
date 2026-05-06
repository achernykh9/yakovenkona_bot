from telebot.types import Message
from loader import bot
from keyboards.inline import get_start_menu
from database import upsert_user, save_event


@bot.message_handler(commands=["start"])
def start(message: Message):
    upsert_user(message.from_user, message.chat.id)
    save_event(message.from_user, message.chat.id, "start")

    name = message.from_user.first_name or "пользователь"
    text = (
        f"Привет, {name}! 👋\n"
        "Я - чат-бот, который поможет Вам:\n"
        "1. Ознакомиться с тарифами услуг 📋\n"
        "2. Подобрать услуги по дизайну интерьера и рассчитать стоимость проекта 💰"
    )
    bot.send_message(message.chat.id, text, reply_markup=get_start_menu())