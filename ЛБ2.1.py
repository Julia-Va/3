class Book:
    def __init__(self, id_, name, pages):
        """Инициализация атрибутов книги."""
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """Возвращает строковое представление книги."""
        return f'Книга "{self.name}"'

    def __repr__(self):
        """Возвращает валидную строку для создания идентичного экземпляра книги."""
        return f'Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})'

# Пример использования класса Book
if __name__ == "__main__":
    book = Book(1, '1984', 328)
    print(book)          # Вывод: Книга "1984"
    print(repr(book))    # Вывод: Book(id_=1, name='1984', pages=328)