class House:                                               # создали класс House

    def __init__(self, name, number_of_floors):  # создали метод __init__ - срабатывает в момент создания объекта класса
        self.name = name                         # Сказали что имя будет равно переданному имени
        self.number_of_floors = number_of_floors  # Сказали что кол-во этаже будет равно переданному переданному кол-ву

    def go_to(self, new_floor):                 # созадли метод go_to - который будет:
        if new_floor < 1 or new_floor > self.number_of_floors: # проверили что этаж не ниже 1 и не выше, чем у нашего здания
            print('Такого этажа не существует')  # Если ниже или выше - выводим на печать "Такого этаже не существует"
        else:                                      # иначе
            for i in range (1, new_floor+1):  #  выводим на печать от 1 до нашего этажа
                print(i)

    def __len__(self):                  # метод считает длину? этажи?
        return self.number_of_floors    # возвращает цифру (этажи)

    def __str__(self):
        return f'Название {self.name}, количество этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(self.number_of_floors, int):
            if self.number_of_floors == other:#.number_of_floors:
                return True
            else:
                return False

    def __lt__(self, other):
        if self.number_of_floors < other: #.number_of_floors:
            return True
        else:
            return False

    def __le__(self, other):
        if self.number_of_floors <= other:# .number_of_floors:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.number_of_floors > other: #.number_of_floors:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.number_of_floors >= other: #.number_of_floors:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.number_of_floors != other:#.number_of_floors:
            return True
        else:
            return False

    def __add__(self, value):
        if isinstance(value, int):
            return self.number_of_floors + value


    def __radd__(self, value):
        if isinstance(value, int):
            return self.number_of_floors + value

    def __iadd__(self, value):
        if isinstance(value, int):
            return self.number_of_floors + value

h1 = House('ЖК Эльюрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1==h2)

h1 = h1 +10

print(h1)
print(h1==h2)

h1 += 10
print(h1)

h2 = 10 + h2
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)
