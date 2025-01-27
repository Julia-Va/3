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
