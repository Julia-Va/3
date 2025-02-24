class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        """
        Инициализация базового класса Vehicle.

        :param make: Производитель автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        """
        self._make = make  # Непубличный атрибут, чтобы предотвратить случайное изменение
        self._model = model  # Непубличный атрибут
        self._year = year  # Непубличный атрибут

    @property
    def make(self) -> str:
        """Возвращает производителя автомобиля."""
        return self._make

    @property
    def model(self) -> str:
        """Возвращает модель автомобиля."""
        return self._model

    @property
    def year(self) -> int:
        """Возвращает год выпуска автомобиля."""
        return self._year

    def honk(self) -> str:
        """Издает звук сигнала автомобиля."""
        return "Бип-бип!"

    def __str__(self) -> str:
        """Возвращает строковое представление транспортного средства."""
        return f'{self.make} {self.model}, {self.year}'

    def __repr__(self) -> str:
        """Возвращает валидную строку для создания идентичного экземпляра транспортного средства."""
        return f'Vehicle(make={repr(self.make)}, model={repr(self.model)}, year={self.year})'


class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, doors: int):
        """
        Инициализация класса Car, дочернего класса от Vehicle.

        :param make: Производитель автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param doors: Количество дверей в автомобиле.
        """
        super().__init__(make, model, year)
        self._doors = doors  # Непубличный атрибут, чтобы предотвратить случайное изменение

    @property
    def doors(self) -> int:
        """Возвращает количество дверей в автомобиле."""
        return self._doors

    def honk(self) -> str:
        """Издает звук сигнала легкового автомобиля.

        Переопределение метода honk для добавления специфичного звука для легкового автомобиля.
        """
        return "Тру-тру!"

    def __str__(self) -> str:
        """Возвращает строковое представление легкового автомобиля."""
        return f'{super().__str__()}, {self.doors} дверей'

    def __repr__(self) -> str:
        """Возвращает валидную строку для создания идентичного экземпляра легкового автомобиля."""
        return f'Car(make={repr(self.make)}, model={repr(self.model)}, year={self.year}, doors={self.doors})'


class Truck(Vehicle):
    def __init__(self, make: str, model: str, year: int, payload_capacity: float):
        """
        Инициализация класса Truck, дочернего класса от Vehicle.

        :param make: Производитель автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param payload_capacity: Грузоподъемность грузовика в тоннах.
        """
        super().__init__(make, model, year)
        self._payload_capacity = payload_capacity  # Непубличный атрибут, чтобы предотвратить случайное изменение

    @property
    def payload_capacity(self) -> float:
        """Возвращает грузоподъемность грузовика."""
        return self._payload_capacity

    def honk(self) -> str:
        """Издает звук сигнала грузовика.

        Переопределение метода honk для добавления специфичного звука для грузовика.
        """
        return "Гудок-гудок!"

    def __str__(self) -> str:
        """Возвращает строковое представление грузовика."""
        return f'{super().__str__()}, грузоподъемность: {self.payload_capacity} тонн'

    def __repr__(self) -> str:
        """Возвращает валидную строку для создания идентичного экземпляра грузовика."""
        return f'Truck(make={repr(self.make)}, model={repr(self.model)}, year={self.year}, payload_capacity={self.payload_capacity})'


# Пример использования классов
if __name__ == "__main__":
    car = Car('Toyota', 'Camry', 2020, 4)
    truck = Truck('Volvo', 'FH', 2018, 18.0)

    print(car)  # Вывод: Toyota Camry, 2020, 4 дверей
    print(repr(car))  # Вывод: Car(make='Toyota', model='Camry', year=2020, doors=4)

    print(truck)  # Вывод: Volvo FH, 2018, грузоподъемность: 18.0 тонн
    print(repr(truck))  # Вывод: Truck(make='Volvo', model='FH', year=2018, payload_capacity=18.0)