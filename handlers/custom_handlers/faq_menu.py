from pathlib import Path
from telebot.types import CallbackQuery, InputMediaPhoto
from loader import bot
from keyboards.inline import get_faq_nav_keyboard
from database import save_event


FAQ_DIR = Path("assets/faq")

@bot.callback_query_handler(func=lambda call: call.data == "faq_menu")
def faq_menu(call: CallbackQuery):
    bot.answer_callback_query(call.id)
    save_event(call.from_user, call.message.chat.id, "faq_menu")
    bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=None
    )

    files = [
        "faq_title.jpg",
        "faq_1.jpg",
        "faq_2.jpg",
        "faq_3.jpg",
        "faq_4.jpg",
        "faq_5.jpg",
        "faq_6.jpg",
        "faq_7.jpg",
    ]

    media = []
    handles = []

    try:
        for i, filename in enumerate(files):
            fh = (FAQ_DIR / filename).open("rb")
            handles.append(fh)
            media.append(InputMediaPhoto(fh))

        bot.send_media_group(call.message.chat.id, media)

    finally:
        for fh in handles:
            try:
                fh.close()
            except Exception:
                pass

    bot.send_message(
        call.message.chat.id,
        "Выберите действие:",
        reply_markup=get_faq_nav_keyboard()
    )