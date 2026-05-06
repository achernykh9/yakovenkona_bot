from telebot.handler_backends import State, StatesGroup

class CalcStates(StatesGroup):
    waiting_area = State()