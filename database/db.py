import os
from pathlib import Path
from peewee import SqliteDatabase

DB_PATH = Path(os.getenv("DATABASE_PATH", "/app/data/bot.db"))
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

db = SqliteDatabase(str(DB_PATH), pragmas={"foreign_keys": 1})