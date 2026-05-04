# data_manager.py

import json
import os

DATA_FILE = "books.json"

def save_books(books_list):
    """
    Сохраняет список книг в файл JSON.
    Принимает список словарей.
    Возвращает кортеж (успех: bool, сообщение: str).
    """
    try:
        # Преобразуем список объектов Book в список словарей для JSON
        data_to_save = [book.to_dict() for book in books_list]
        
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=4)
        return True, "Данные успешно сохранены в books.json"
    
    except Exception as e:
        return False, f"Ошибка при сохранении файла: {e}"


def load_books():
    """
    Загружает список книг из файла JSON.
    Возвращает кортеж (успех: bool, данные: list или сообщение об ошибке).
    """
    try:
        if not os.path.exists(DATA_FILE):
            return False, "Файл books.json не найден. Будет создан при первом сохранении."
        
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # Преобразуем список словарей в список объектов Book
        books_list = [Book.from_dict(item) for item in data]
        return True, books_list

    except json.JSONDecodeError:
        return False, "Ошибка декодирования JSON. Файл может быть поврежден."
    except Exception as e:
        return False, f"Неизвестная ошибка при загрузке: {e}"
