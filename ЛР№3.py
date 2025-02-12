class Book:
    def __init__(self, name, author):
        """Инициализация базовых атрибутов книги."""
        self._name = name
        self._author = author

    @property
    def name(self):
        """Возвращает название книги."""
        return self._name

    @property
    def author(self):
        """Возвращает автора книги."""
        return self._author

    def __str__(self):
        """Возвращает строковое представление книги."""
        return f'Книга "{self.name}" автор: {self.author}'

    def __repr__(self):
        """Возвращает валидную строку для создания идентичного экземпляра книги."""
        return f'Book(name={repr(self.name)}, author={repr(self.author)})'


class PaperBook(Book):
    def __init__(self, name, author, pages):
        """Инициализация атрибутов бумажной книги."""
        super().__init__(name, author)
        self.pages = pages  # Используем свойство для валидации

    @property
    def pages(self):
        """Возвращает количество страниц книги."""
        return self._pages

    @pages.setter
    def pages(self, value):
        """Устанавливает количество страниц с проверкой на корректность."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __str__(self):
        """Возвращает строковое представление бумажной книги."""
        return f'Бумажная книга "{self.name}" автор: {self.author}, страницы: {self.pages}'

    def __repr__(self):
        """Возвращает валидную строку для создания идентичного экземпляра бумажной книги."""
        return f'PaperBook(name={repr(self.name)}, author={repr(self.author)}, pages={self.pages})'


class AudioBook(Book):
    def __init__(self, name, author, duration):
        """Инициализация атрибутов аудиокниги."""
        super().__init__(name, author)
        self.duration = duration  # Используем свойство для валидации

    @property
    def duration(self):
        """Возвращает продолжительность аудиокниги."""
        return self._duration

    @duration.setter
    def duration(self, value):
        """Устанавливает продолжительность с проверкой на корректность."""
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = float(value)

    def __str__(self):
        """Возвращает строковое представление аудиокниги."""
        return f'Аудиокнига "{self.name}" автор: {self.author}, продолжительность: {self.duration} часов'

    def __repr__(self):
        """Возвращает валидную строку для создания идентичного экземпляра аудиокниги."""
        return f'AudioBook(name={repr(self.name)}, author={repr(self.author)}, duration={self.duration})'


# Пример использования классов
if __name__ == "__main__":
    paper_book = PaperBook('Война и мир', 'Лев Толстой', 1225)
    audio_book = AudioBook('1984', 'Джордж Оруэлл', 11.5)

    print(paper_book)  # Вывод: Бумажная книга "Война и мир" автор: Лев Толстой, страницы: 1225
    print(repr(paper_book))  # Вывод: PaperBook(name='Война и мир', author='Лев Толстой', pages=1225)

    print(audio_book)  # Вывод: Аудиокнига "1984" автор: Джордж Оруэлл, продолжительность: 11.5 часов
    print(repr(audio_book))  # Вывод: AudioBook(name='1984', author='Джордж Оруэлл', duration=11.5)