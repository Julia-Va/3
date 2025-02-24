class Library:
    def __init__(self, books=None):
        """Инициализация атрибутов библиотеки."""
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        """Возвращает следующий доступный идентификатор для добавления новой книги."""
        if not self.books:
            return 1
        else:
            return max(book.id for book in self.books) + 1

    def get_index_by_book_id(self, book_id):
        """Возвращает индекс книги в списке по её идентификатору."""
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")
# Пример использования класса Library
if __name__ == "__main__":
    # Создание экземпляра библиотеки
    library = Library()

    # Создание книг
    book1 = Book(1, '1984', 328)
    book2 = Book(2, 'Дневник Анны Франк', 300)

    # Добавление книг в библиотеку
    library.books.append(book1)
    library.books.append(book2)

    # Получение следующего идентификатора для новой книги
    next_id = library.get_next_book_id()
    print(f'Следующий идентификатор для новой книги: {next_id}')  # Вывод: 3

    # Получение индекса книги по идентификатору
    try:
        index = library.get_index_by_book_id(1)
        print(f'Индекс книги с id 1: {index}')  # Вывод: 0
    except ValueError as e:
        print(e)

    # Попробуем получить индекс несуществующей книги
    try:
        index = library.get_index_by_book_id(3)
    except ValueError as e:
        print(e)  # Вывод: Книги с запрашиваемым id не существует
