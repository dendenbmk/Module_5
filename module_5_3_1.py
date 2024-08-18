class House:                                         # Создали Kласс House
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