class Cake():
    def __init__(self):
        self.flavour = ""
        self.size = 100
    
    def set_flavour(self, flavour):
        self.flavour = flavour
    
    def take_slice(self, slice):
        self.size -= slice
        print(f"You have taken a {slice} percent sized slice. \n There is {self.size} percent cake remaining.")

class Baker():
    def __init__(self):
        self.stomach_space_remaining = 100
        # You can only eat up to 100 sections of cake in one sitting.
        self.cakes_sampled = []
        # You must sample at least 5 cakes in order to ensure quality!
    
    def eat_cake(self, cake, slice):
        cake.take_slice(slice)
        if cake in self.cakes_sampled:
            print("You've tried this one already!")
        else:
            self.cakes_sampled.append(cake)
            self.stomach_space_remaining -= slice


    def check_space(self):
        print(f"You have eaten {len(self.cakes_sampled)} cakes. \n You have {self.stomach_space_remaining} percent space remaining in your belly!")
        if len(self.cakes_sampled) > 4:
            print("You have sampled more than enough cake. Time to open the shop!")
            exit()
        elif self.stomach_space_remaining < 0:
            print("You have filled up on too much cake. You pass out. The shop makes no business this day.")
            exit()
        
        return self.stomach_space_remaining

    def cakes(self):
        for cake in self.cakes_sampled:
            print(str(self.cakes_sampled.index(cake)+1) + ": " + cake.flavour)


    def choose_favourite(self):
        print("Which was your favourite cake?")
        self.cakes()
        print("Pick the number as it appears in the list.")
        choice = int(input("Which cake?: \n")) - 1
        return f"{self.cakes_sampled[choice].flavour} was your favourite!"

# everything that you write here, is acting upon the 'main' object