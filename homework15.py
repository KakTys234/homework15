class Building:
    def __init__(self, buildingType, numberOfFloors):
        self.buildingType = buildingType
        self.numberOfFloors = numberOfFloors
        self.say_info()

    def say_info(self):
        print(f'Название: {self.buildingType}, Количество этажей: {self.numberOfFloors}')

    def __eq__(self, other):
        return self.buildingType == other.buildingType and self.numberOfFloors == other.numberOfFloors

h1 = Building('Орион', 23)
h2 = Building('Объект', 25)
print(h1 == h2)