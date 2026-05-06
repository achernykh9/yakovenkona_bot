from peewee import SqliteDatabase

db = SqliteDatabase("bot.db", pragmas={"foreign_keys": 1})