import sys
import json
from pathlib import Path
from database.db import db
from database.models import User, History

def print_user(user):
    print(
        f"user_id={user.user_id}, "
        f"chat_id={user.chat_id}, "
        f"first_name={user.first_name}, "
        f"username={user.username}, "
        f"created_at={user.created_at}"
    )

def print_history_item(item):
    payload = item.payload
    if payload:
        try:
            payload = json.loads(payload)
        except Exception:
            pass
    print(
        f"id={item.id}, "
        f"user_id={item.user.user_id}, "
        f"event_type={item.event_type}, "
        f"payload={payload}, "
        f"created_at={item.created_at}"
    )

def count_users():
    print("Пользователей:", User.select().count())

def count_events():
    print("Событий:", History.select().count())

def list_users(limit=10):
    query = User.select().order_by(User.created_at.desc()).limit(limit)
    for user in query:
        print_user(user)

def list_events(limit=20):
    query = History.select().order_by(History.created_at.desc()).limit(limit)
    for item in query:
        print_history_item(item)

def history_by_user_id(user_id, limit=50):
    user = User.get_or_none(User.user_id == user_id)
    if not user:
        print("Пользователь не найден")
        return

    print_user(user)
    print("\nИстория:")
    query = History.select().where(History.user == user).order_by(History.created_at.desc()).limit(limit)
    for item in query:
        print_history_item(item)

def help_text():
    print("""
Использование:
  python admin_db.py count-users
  python admin_db.py count-events
  python admin_db.py list-users
  python admin_db.py list-events
  python admin_db.py history <user_id>

Примеры:
  python admin_db.py count-users
  python admin_db.py history 123456789
""".strip())

def main():
    if len(sys.argv) < 2:
        help_text()
        return

    command = sys.argv[1].lower()

    db.connect(reuse_if_open=True)
    try:
        if command == "count-users":
            count_users()
        elif command == "count-events":
            count_events()
        elif command == "list-users":
            list_users()
        elif command == "list-events":
            list_events()
        elif command == "history":
            if len(sys.argv) < 3:
                print("Нужно указать user_id")
                return
            try:
                user_id = int(sys.argv[2])
            except ValueError:
                print("user_id должен быть числом")
                return
            history_by_user_id(user_id)
        else:
            print("Неизвестная команда")
            help_text()
    finally:
        db.close()

if __name__ == "__main__":
    main()