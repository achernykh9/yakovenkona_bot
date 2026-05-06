from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_calc_menu():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Планировочное решение", callback_data="calc_planning"))
    keyboard.add(InlineKeyboardButton("Технический проект", callback_data="calc_technical"))
    keyboard.add(InlineKeyboardButton("Дизайн-проект", callback_data="calc_design"))
    keyboard.add(InlineKeyboardButton("Хоумстейджинг", callback_data="calc_home"))
    keyboard.add(InlineKeyboardButton("🏠 В начало", callback_data="go_home"))
    return keyboard