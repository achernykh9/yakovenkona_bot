import json
from .db import db
from .models import User, History

def create_tables():
    db.connect(reuse_if_open=True)
    db.create_tables([User, History], safe=True)
    db.close()

def upsert_user(tg_user, chat_id):
    db.connect(reuse_if_open=True)
    user, created = User.get_or_create(
        user_id=tg_user.id,
        defaults={
            "chat_id": chat_id,
            "first_name": tg_user.first_name,
            "username": tg_user.username,
        },
    )
    if not created:
        user.chat_id = chat_id
        user.first_name = tg_user.first_name
        user.username = tg_user.username
        user.save()
    db.close()
    return user

def save_event(tg_user, chat_id, event_type, payload=None):
    db.connect(reuse_if_open=True)
    user, _ = User.get_or_create(
        user_id=tg_user.id,
        defaults={
            "chat_id": chat_id,
            "first_name": tg_user.first_name,
            "username": tg_user.username,
        },
    )
    if user.chat_id != chat_id or user.first_name != tg_user.first_name or user.username != tg_user.username:
        user.chat_id = chat_id
        user.first_name = tg_user.first_name
        user.username = tg_user.username
        user.save()
    History.create(
        user=user,
        event_type=event_type,
        payload=json.dumps(payload, ensure_ascii=False) if payload is not None else None,
    )
    db.close()

def save_user_message(message):
    save_event(
        message.from_user,
        message.chat.id,
        "user_message",
        {"text": message.text, "message_id": message.message_id},
    )