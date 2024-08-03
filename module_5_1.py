class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, namber_of_want_floor):
        self.number_of_floors
        if namber_of_want_floor > self.number_of_floors or namber_of_want_floor < 1:
            print('Такого этажа не существует')
        else:
            print(namber_of_want_floor)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(20)
h2.go_to(2)