import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
if dotenv_path:
    load_dotenv(dotenv_path)

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN не задан в переменных окружения")

DEFAULT_COMMANDS = [
    ("start", "Запустить бота"),
]