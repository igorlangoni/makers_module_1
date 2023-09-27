from random import random as rand
from time import sleep 

completed = 0


class Cake():
    def __init__(self):
        self.flavour = ""
        self.size = 100
    
    def set_flavour(self, flavour):
        self.flavour = flavour
    
    def take_slice(self, slice):
        self.size -= slice
        print(f"You have taken a {slice} percent sized slice. \n There is {self.size} percent cake remaining.")


class Order():

    def __init__(self):
        self.flavour = self.flavour_rand()
        self.size = round(rand() * 100)

    def flavour_rand(self):
        rand_perc = round(rand() * 100)
        if rand_perc > 80:
            return "Strawberry"
        elif rand_perc > 60:
            return "Vanilla"
        elif rand_perc > 40:
            return "Chocolate"
        elif rand_perc > 20:
            return "Banana"
        else:
            return "Carrot"

    def satisfy_order(self, cake):
        global completed
        if cake.flavour == self.flavour:
            print("The flavour is correct!")
            sleep(3)
            if cake.size == self.size:
                print("The size is correct. Order Satisfied")
                sleep(3)
                completed += 1
                print(f"You have #:{completed} orders left before opening time!")
                sleep(3)
                if completed > 5:
                    complete()
                order = run_order()

        else:
            print("That isn't right!")


def run_order():
    order = Order()
    print(f"You have a new order! A {order.flavour} flavour cake that is {order.size} size!")
    return order


def complete():
    print("You have finished today's orders! EXCELLENT!")
    exit()


def run():
    order = run_order()
    print(f"Your order is ready! Order is a {order.size} sized, {order.flavour} cake! ")
    sleep(3)

    return order

order = run()

# Run bakery_2 with `python3 -i bakery_2.py`

