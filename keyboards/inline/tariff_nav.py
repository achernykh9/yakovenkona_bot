from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_tariff_nav_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("↩️ Назад", callback_data="back_to_tariffs_info"))
    keyboard.add(InlineKeyboardButton("🏠 В начало", callback_data="go_home"))
    keyboard.add(InlineKeyboardButton("💬 Связаться с дизайнером", url="https://t.me/yakovenkona"))
    return keyboard