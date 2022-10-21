# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Room:
    def get_name(self):
        return 42


class Street:
    def get_room(self) -> Room:
        return Room()


class City:
    def get_street(self) -> Street:
        return Street()

    def population(self):
        return 100500


class Country:
    def get_city(self) -> City:
        return City()


class Planet:
    def get_contry(self) -> Country:
        return Country()


class Person:
    def __init__(self, number_room=Room().get_name(), city_population=City().population()):
        self.number_room = number_room
        self.city_population = city_population

    def get_person_room(self):
        return self.number_room

    def get_city_population(self):
        return self.city_population


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.

print('Первый житель:')
first = Person()
print(first.get_person_room())
print(first.get_city_population())

print('\nВторой житель:')
second = Person(number_room=2, city_population=333)
print(second.get_person_room())
print(second.get_city_population())
