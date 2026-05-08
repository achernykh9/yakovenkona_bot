from datetime import datetime
from peewee import Model, BigIntegerField, CharField, DateTimeField, ForeignKeyField, TextField
from .db import db

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    user_id = BigIntegerField(unique=True)
    chat_id = BigIntegerField()
    first_name = CharField(max_length=255, null=True)
    username = CharField(max_length=255, null=True)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        table_name = "users"

class History(BaseModel):
    user = ForeignKeyField(User, backref="history", on_delete="CASCADE")
    event_type = CharField(max_length=64)
    payload = TextField(null=True)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        table_name = "history"