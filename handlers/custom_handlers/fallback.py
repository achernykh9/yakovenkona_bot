from telebot.types import Message
from loader import bot
from database import upsert_user, save_user_message


@bot.message_handler(content_types=["text"], chat_types=["private"])
def save_all_user_messages(message: Message):
    if message.text.startswith("/"):
        return

    if bot.get_state(message.from_user.id, message.chat.id) is not None:
        return

    upsert_user(message.from_user, message.chat.id)
    save_user_message(message)