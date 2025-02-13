class House:                                         # Создали Kласс House
    def __init__(self, name, number_of_floors):  # обьявили, что класс будет иметь (пока) 2 атрибута, имя и кол. этажей
        self.name = name                         # Собственное имя будет - именем
        self.number_of_floors = number_of_floors     # изначальное количество этажей


    def go_to(self, namber_of_want_floor):       # Создали метод go_to, куда будем передовать кол-во этажей при вызове
        if namber_of_want_floor > self.number_of_floors or namber_of_want_floor < 1:  # если передадим желаемый этаж
                                                   # больше чем number_of_floors или меньше 1, то ...
            print('Такого этажа не существует')    #  будет выводиться это сообщение
        else:                                      # иначе...
            for i in range(1, namber_of_want_floor + 1): # перебераем числа (этажы) от 1 до нужного...
                print(i)                                     # и выводим в консоль

    def __len__(self):                     # Создали метод (волшебный) который возвращает кол-во этажей беря его из ...
        return self.number_of_floors             # ... атрибута number_of_floors

    def __str__(self):                        # # Создали метод (волшебный) который возвращает строку с названием и ...
        return f' Название: {self.name}, кол-во этажей: {self.number_of_floors}'  # ... кол-вом этажей

h1 = House('ЖК Эльбрус', 10)  # создали переменную в которой создали переменные нашего класса
h2 = House('ЖК Акация', 20)

# __str__
print(h1)                                         # вывели на печать ранее созданую переменную
print(h2)

# __len__
print(len(h1))          # вывели на печать ранее созданный 'волшебный' метод (len) куда отправили нашу переменную (h1)
print(len(h2))

print(str(h1))           # вывели на печать ранее созданный 'волшебный'метод (str) куда отправили нашу переменную (h1)
