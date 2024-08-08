class House:                                         # Создали Kласс House
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)


    def __init__(self, name, number_of_floors):  # обьявили, что класс будет иметь (пока) 2 атрибута, имя и кол. этажей
        self.name = name                         # Собственное имя будет - именем
        self.number_of_floors = number_of_floors     # изначальное количество этажей


    def go_to(self, namber_of_want_floor):       # Создали метод go_to, куда будем передовать кол-во этажей при вызове
        self.number_of_floors                    # сделали доступным глобальный атрибут   number_of_floors
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
        return self.number_of_floors < other.number_of_floors

    def __eq__(self, other):
        if self.number_of_floors == other.number_of_floors:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.number_of_floors < other.number_of_floors:
            return True
        else:
            return False

    def __le__(self, other):
        if self.number_of_floors <= other.number_of_floors:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.number_of_floors > other.number_of_floors:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.number_of_floors >= other.number_of_floors:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.number_of_floors != other.number_of_floors:
            return True
        else:
            return False

    def __add__(self, other):
        if isinstance(self.number_of_floors, int):
            self.number_of_floors += int(other)
            return self

    def __radd__(self, other):
        self.number_of_floors += int(other)
        return self

    def __iadd__(self, other):
        self.number_of_floors += int(other)
        return self

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)