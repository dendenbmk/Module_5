class House:                                         # Создали Kласс House
    def __init__(self, name, number_of_floors):  # обьявили, что класс будет иметь (пока) 2 атрибута, имя и кол. этажей
        self.name = name                         # Собственное имя будет - именем
        self.number_of_floors = number_of_floors     # изначальное количество этажей


    def go_to(self, namber_of_want_floor):       # Создали метод go_to, куда будем передовать кол-во этажей при вызове
        self.number_of_floors                    # сделали доступным глобальный атрибут   number_of_floors
        if isinstance(self.number_of_floors, int):
            if namber_of_want_floor > self.number_of_floors or namber_of_want_floor < 1:  # если передадим желаемый этаж
                                                   # больше чем number_of_floors или меньше 1, то ...
                print('Такого этажа не существует')    #  будет выводиться это сообщение
            else:                                      # иначе...
                print(namber_of_want_floor)            # выведим желаемый этаж


    def __len__(self):                     # Создали метод (волшебный) который возвращает кол-во этажей беря его из ...
        return self.number_of_floors             # ... атрибута number_of_floors


    def __str__(self):                        # # Создали метод (волшебный) который возвращает строку с названием и ...
        return f' Название: {self.name}, кол-во этажей: {self.number_of_floors}'  # ... кол-вом этажей


    def __lt__(self, other):
        if isinstance(self.number_of_floors, int):
            return self.number_of_floors < other.number_of_floors

    def __eq__(self, other):
        if isinstance(self.number_of_floors, int):
            if self.number_of_floors == other.number_of_floors:
                return True
            else:
                return False

    def __lt__(self, other):
        if isinstance(self.number_of_floors, int):
            if self.number_of_floors < other.number_of_floors:
                return True
            else:
                return False

    def __le__(self, other):
        if isinstance(self.number_of_floors, int):
            if self.number_of_floors <= other.number_of_floors:
                return True
            else:
                return False

    def __gt__(self, other):
        if isinstance(self.number_of_floors, int):
            if self.number_of_floors > other.number_of_floors:
                return True
            else:
                return False

    def __ge__(self, other):
        if isinstance(self.number_of_floors, int):
            if self.number_of_floors >= other.number_of_floors:
                return True
            else:
                return False

    def __ne__(self, other):
        if isinstance(self.number_of_floors, int):
            if self.number_of_floors != other.number_of_floors:
                return True
            else:
                return False

    def __add__(self, other):
        if isinstance(self.number_of_floors, int):
            self.number_of_floors += int(other)
            return self

    def __radd__(self, other):
        if isinstance(self.number_of_floors, int):
            self.number_of_floors += int(other)
            return self

    def __iadd__(self, other):
        if isinstance(self.number_of_floors, int):
            self.number_of_floors += int(other)
            return self

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
