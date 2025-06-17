class Pizza:
    # Pizza objects and associated cost
    def __init__(self, crust, sauce, toppings):
        #initialize a pizza
        # set pizza variables
        self.crust = crust
        self.sauce = sauce
        self.cheese = "mozzerella"
        self.toppings = toppings
        # set cost to create
        self.cost = 0
    
    def __str__(self):
        return("Your pizza has:" + 
               "\n crust: " + self.crust + 
               "\n sauce: " + self.sauce + 
               "\n cheese: " + self.cheese + 
               "\n and" + 
               "\n toppings: " + (", " .join(self.toppings)) +
               "\n cost is: " + str(self.cost))
    
    def total_cost(self):
        # cost of crust
        if self.crust == "thin":
            self.cost = self.cost + 5
        if self.crust == "thick":
            self.cost = self.cost + 6
        if self.crust == "gluten free":
            self.cost = self.cost + 8
        
        # cost of sauce
        if self.sauce == "marinara":
            self.cost = self.cost + 2
        if self.sauce == "pesto":
            self.cost = self.cost + 3
        if self.sauce == "Liv Sauce":
            self.cost = self.cost + 5
        
        # cost of topping
        for topping in self.toppings:
            if topping == "pineapple":
                self.cost = self.cost + 1
            if topping == "pepperoni":
                self.cost = self.cost + 2
            if topping == "mushrooms":
                self.cost = self.cost + 3
        
        

my_pizza = Pizza("thin", "marinara", ["pineapple", "pepperoni"])
my_pizza.total_cost()
print(my_pizza.__str__())