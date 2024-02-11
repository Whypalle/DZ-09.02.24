import random
class Person:
    def __init__(self, name, age, strength, agility):
        self.name = name
        self.age = age
        self.strength = strength
        self.agility = agility

    def attack(self, target):
        damage = self.strength * 5
        print(f"{self.name} атаковал {target} и нанес {damage} единиц урона.")

    def dodge(self):
        agility_chance = self.agility * 0.1
        if random.uniform(0, 1) < agility_chance:
            print(f"{self.name} уклонился от атаки.")
        else:
            print(f"{self.name} не смог уклониться от атаки.")

    def speak(self, message):
        print(f"{self.name} говорит: '{message}'.")


# Создание персонажей
person1 = Person("Иван", 25, 10, 5)
person2 = Person("Анна", 30, 8, 7)

# Использование способностей персонажей
person1.attack(person2.name)
person2.dodge()


