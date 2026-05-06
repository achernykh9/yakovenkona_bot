import re
from telebot.types import Message
from loader import bot
from states.calc_states import CalcStates
from keyboards.inline import get_calc_nav_keyboard
from database import save_event


def format_money(value):
    return f"{value:,.2f}".replace(",", " ")

def calculate_price(tariff_code, area):
    if tariff_code == "planning":
        return 30000 if area < 50 else area * 600
    if tariff_code == "technical":
        return 80000 if area < 50 else area * 1600
    if tariff_code == "design":
        return 120000 if area < 50 else area * 2400
    if tariff_code == "home":
        return 70000 if area < 50 else area * 1400
    return 0

@bot.message_handler(state=CalcStates.waiting_area, content_types=["text"])
def calc_area_input(message: Message):
    text = message.text.strip().replace(",", ".")
    if not re.fullmatch(r"\d+(\.\d+)?", text):
        save_event(message.from_user, message.chat.id, "calc_area_invalid", {"text": message.text})
        bot.send_message(message.chat.id, "Некорректный ввод: введите целое число или десятичную дробь")
        return

    area = float(text)
    if area < 1 or area > 3000:
        save_event(message.from_user, message.chat.id, "calc_area_invalid", {"text": message.text})
        bot.send_message(message.chat.id, "Некорректный ввод: введите целое число или десятичную дробь от 1 до 3000")
        return

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        tariff_name = data.get("tariff_name", "тариф")
        tariff_code = data.get("tariff_code")
        prompt_message_id = data.get("prompt_message_id")

    save_event(message.from_user, message.chat.id, "calc_area_input", {"area": area, "tariff_code": tariff_code})

    if prompt_message_id:
        try:
            bot.edit_message_reply_markup(
                chat_id=message.chat.id,
                message_id=prompt_message_id,
                reply_markup=None
            )
        except Exception:
            pass

    price = calculate_price(tariff_code, area)
    price_text = format_money(price)

    save_event(
        message.from_user,
        message.chat.id,
        "calc_result",
        {"tariff_code": tariff_code, "area": area, "price": price},
    )

    result_text = (
        f'✅ Готово! Предварительная стоимость услуги "{tariff_name}" - {price_text} ₽\n\n'
        "📄 Для проекта необходимо предоставить:\n"
        "1. Обмерный план (замеры выполняются самостоятельно или специалистами);\n"
        "2. План БТИ или план от застройщика;\n"
        "3. Референсы (примеры интерьеров в картинках).\n\n"
        '📩 Если готовы заказать проект или остались вопросы, нажмите на кнопку "Связаться с дизайнером" ниже'
    )

    bot.send_message(message.chat.id, result_text, reply_markup=get_calc_nav_keyboard())
    bot.delete_state(message.from_user.id, message.chat.id)