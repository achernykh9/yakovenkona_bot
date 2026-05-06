from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_start_menu():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Подробнее о тарифах", callback_data="tariffs_info_menu"))
    keyboard.add(InlineKeyboardButton("Рассчитать стоимость услуг", callback_data="calc_services_menu"))
    keyboard.add(InlineKeyboardButton("Частые вопросы", callback_data="faq_menu"))
    return keyboard