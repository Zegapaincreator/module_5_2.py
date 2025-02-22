class House:
    def __init__(self, name, max_floors):
        self.name = name
        self.number_of_floors = max_floors

    def go_to(self, new_floor):
        if not (new_floor in range(1, self.number_of_floors+1)):
            print("Такого этажа не существует!")
            return
        for floor in range(1, new_floor+1):
            print(floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

h1 = House('ЖК Горский', 10)
h2 = House('Домик в деревне', 20)

h1.go_to(5)
h2.go_to(10)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))