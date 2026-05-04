import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

# --- Основные данные ---
books = []

# --- Функции логики ---
def validate_input():
    title = title_entry.get().strip()
    author = author_entry.get().strip()
    genre = genre_entry.get().strip()
    pages = pages_entry.get().strip()

    if not (title and author and genre and pages):
        messagebox.showerror("Ошибка", "Все поля обязательны для заполнения!")
        return False
    if not pages.isdigit():
        messagebox.showerror("Ошибка", "Количество страниц должно быть целым числом!")
        return False
    return True

def add_book():
    if validate_input():
        book = {
            "title": title_entry.get(),
            "author": author_entry.get(),
            "genre": genre_entry.get(),
            "pages": int(pages_entry.get())
        }
        books.append(book)
        update_table()
        clear_entries()

def clear_entries():
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    genre_entry.delete(0, tk.END)
    pages_entry.delete(0, tk.END)

def update_table(filtered_books=None):
    for i in tree.get_children():
        tree.delete(i)
    data = filtered_books if filtered_books is not None else books
    for book in data:
        tree.insert("", tk.END, values=(book["title"], book["author"], book["genre"], book["pages"]))

def filter_books():
    filtered = books.copy()
    
    genre = filter_genre.get().strip()
    if genre:
        filtered = [b for b in filtered if b["genre"].lower() == genre.lower()]
    
    pages = filter_pages.get().strip()
    if pages.isdigit():
        filtered = [b for b in filtered if b["pages"] > int(pages)]
    
    update_table(filtered)

def save_books():
    if not books:
        messagebox.showinfo("Информация", "Нет данных для сохранения.")
        return
    try:
        with open("books.json", "w", encoding="utf-8") as f:
            json.dump(books, f, ensure_ascii=False, indent=4)
        messagebox.showinfo("Успех", "Данные успешно сохранены в books.json")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")

def load_books():
    global books
    try:
        with open("books.json", "r", encoding="utf-8") as f:
            books = json.load(f)
        update_table()
        messagebox.showinfo("Успех", "Данные успешно загружены из books.json")
    except FileNotFoundError:
        messagebox.showinfo("Информация", "Файл books.json не найден.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при загрузке файла: {e}")

# --- Создание окна ---
root = tk.Tk()
root.title("Book Tracker")
root.geometry("700x500")

# --- Ввод данных ---
tk.Label(root, text="Название книги:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
title_entry = tk.Entry(root, width=40)
title_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

tk.Label(root, text="Автор:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
author_entry = tk.Entry(root, width=40)
author_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

tk.Label(root, text="Жанр:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
genre_entry = tk.Entry(root, width=40)
genre_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

tk.Label(root, text="Страниц:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
pages_entry = tk.Entry(root, width=10)
pages_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

add_btn = tk.Button(root, text="Добавить книгу", command=add_book)
add_btn.grid(row=4, column=0, columnspan=2, pady=10)

# --- Таблица ---
tree = ttk.Treeview(root, columns=("title", "author", "genre", "pages"), show="headings")
tree.heading("title", text="Название")
tree.heading("author", text="Автор")
tree.heading("genre", text="Жанр")
tree.heading("pages", text="Страниц")
tree.column("pages", width=80)
tree.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

# Настройка сетки для растягивания таблицы
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(1, weight=1)

# --- Фильтрация ---
tk.Label(root, text="Фильтр по жанру:").grid(row=6, column=0, padx=5, pady=5, sticky="e")
filter_genre = tk.Entry(root)
filter_genre.grid(row=6, column=1, padx=5, pady=5, sticky="w")

tk.Label(root, text="Больше страниц:").grid(row=7, column=0, padx=5, pady=5, sticky="e")
filter_pages = tk.Entry(root)
filter_pages.grid(row=7, column=1, padx=5, pady=5, sticky="w")

filter_btn = tk.Button(root, text="Фильтровать", command=filter_books)
filter_btn.grid(row=8, column=0, columnspan=2)

# --- Сохранение и загрузка ---
save_btn = tk.Button(root, text="Сохранить в JSON", command=save_books)
save_btn.grid(row=9, column=0)
load_btn = tk.Button(root, text="Загрузить из JSON", command=load_books)
load_btn.grid(row=9, column=1)

root.mainloop()