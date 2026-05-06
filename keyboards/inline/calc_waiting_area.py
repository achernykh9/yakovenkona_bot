from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_calc_waiting_area_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("↩️ Назад", callback_data="calc_back"))
    keyboard.add(InlineKeyboardButton("🏠 В начало", callback_data="go_home"))
    return keyboard