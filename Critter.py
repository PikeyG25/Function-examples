#Parker Gowans
#1/19

import time
import pickle
class Critter(object):
    """A Virtual Pet"""
    def __init__(self, name, hunger, boredom):
        print("A new critter has been born")
        self.__name = name
        self.__hunger = hunger
        self.__boredom = boredom

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("A critter's name can't be the empty string.")
        else:
            self.__name = new_name
            print("Name change successful. ")

    def talk(self):
        print("\nHi, I'm", self.__name)


    def __pass_time(self):
        self.hunger = self.hunger + 1
        self.boredom = self.boredom + 1

    def play(self):

        if self.boredom<0:
            self.boredom = 0

        else:
            self.__pass_time

    def talk(self):
        """"""
        self.__pass_time()

    def eat(self):
        self.hunger -=food
        if self.hunger < 0:
            self.hunger = 0

        else:
            self.__pass_time(self)

def main(object):
    get.critter_name
    choice = None
    while choice != 0:
        """MENU"""
        choice = input("Pick a choice - 0. Exit - 1. Talk - 2. Eat - 3. Play")
        if choice == 0:
            print("Goodbye")
        elif choice == 1:
            crit.talk()
        elif choice == 2:
            crit.eat()
        elif choice == 3:
            crit.play()
        else:
            print("Not a good choice")





