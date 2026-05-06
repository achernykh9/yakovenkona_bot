from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_tariffs_info_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Планировочное решение", callback_data="tariff_info_planning"))
    keyboard.add(InlineKeyboardButton("Технический проект", callback_data="tariff_info_technical"))
    keyboard.add(InlineKeyboardButton("Дизайн-проект", callback_data="tariff_info_design"))
    keyboard.add(InlineKeyboardButton("Хоумстейджинг", callback_data="tariff_info_home"))
    keyboard.add(InlineKeyboardButton("Комплектация", callback_data="tariff_info_complect"))
    keyboard.add(InlineKeyboardButton("🏠 В начало", callback_data="go_home"))
    return keyboard