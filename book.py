# book.py

class Book:
    """
    Класс для представления книги.
    Хранит информацию о названии, авторе, жанре и количестве страниц.
    """
    def __init__(self, title: str, author: str, genre: str, pages: int):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages

    def to_dict(self) -> dict:
        """
        Преобразует объект Book в словарь для сохранения в JSON.
        """
        return {
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "pages": self.pages
        }

    @staticmethod
    def from_dict(data: dict):
        """
        Создает объект Book из словаря (при загрузке из JSON).Конечно, вот подробная реализация проекта с разделением на файлы согласно предложенной структуре.

### Структура проекта
