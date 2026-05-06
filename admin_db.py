import json
from database import db, User, History

def show_menu():
    print("\nКоманды:")
    print("1 - Количество пользователей")
    print("2 - Количество событий")
    print("3 - Список последних пользователей")
    print("4 - История по user_id")
    print("5 - Последние события")
    print("0 - Выход")

def print_user(user):
    print(
        f"user_id={user.user_id}, "
        f"chat_id={user.chat_id}, "
        f"name={user.first_name}, "
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
        f"created_at={item.created_at}, "
        f"event_type={item.event_type}, "
        f"payload={payload}"
    )

def count_users():
    print("Пользователей:", User.select().count())

def count_history():
    print("Событий:", History.select().count())

def last_users(limit=10):
    query = User.select().order_by(User.created_at.desc()).limit(limit)
    for user in query:
        print_user(user)

def history_by_user_id(user_id, limit=50):
    user = User.get_or_none(User.user_id == user_id)
    if not user:
        print("Пользователь не найден")
        return
    print_user(user)
    print("\nИстория:")
    query = user.history.order_by(History.created_at.desc()).limit(limit)
    for item in query:
        print_history_item(item)

def last_events(limit=20):
    query = History.select().order_by(History.created_at.desc()).limit(limit)
    for item in query:
        print_history_item(item)

def main():
    db.connect(reuse_if_open=True)
    try:
        while True:
            show_menu()
            choice = input("\nВыберите пункт: ").strip()

            if choice == "1":
                count_users()
            elif choice == "2":
                count_history()
            elif choice == "3":
                last_users()
            elif choice == "4":
                user_id = int(input("Введите user_id: ").strip())
                history_by_user_id(user_id)
            elif choice == "5":
                last_events()
            elif choice == "0":
                break
            else:
                print("Неизвестная команда")
    finally:
        db.close()

if __name__ == "__main__":
    main()