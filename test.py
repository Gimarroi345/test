import hashlib

# Простая база данных: имя пользователя и хеш пароля
users_db = {}

def hash_password(password: str) -> str:
    """Создаёт хеш пароля с помощью SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username: str, password: str) -> None:
    """Регистрация нового пользователя."""
    if username in users_db:
        print("Пользователь уже существует.")
        return
    users_db[username] = hash_password(password)
    print(f"Пользователь {username} успешно зарегистрирован.")

def authenticate_user(username: str, password: str) -> bool:
    """Проверка логина и пароля."""
    if username not in users_db:
        print("Пользователь не найден.")
        return False
    hashed = hash_password(password)
    if users_db[username] == hashed:
        print("Аутентификация успешна!")
        return True
    else:
        print("Неверный пароль.")
        return False

def main():
    while True:
        print("\n1. Зарегистрироваться\n2. Войти\n3. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            register_user(username, password)

        elif choice == "2":
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            authenticate_user(username, password)

        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
