from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self) -> None:
        pass


class Dog(Animal):
    def speak(self) -> None:
        print("Гав!")


class Cat(Animal):
    def speak(self) -> None:
        print("Мяу!")


class AnimalFactory:
    def create_animal(self, name: str) -> Animal:
        if name.lower() == "dog":
            return Dog()

        if name.lower() == "cat":
            return Cat()

        raise ValueError("Неизвестное животное")