class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def go_to(self, new_floor):
        for i in range(new_floor + 1):
            if new_floor > self.numbers_of_floors:
                print('Такого этажа не существует')
                break
            if i > 0:
                print(i)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

