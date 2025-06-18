"""This module generates a Pizza object"""

class Pizza:
    """This is a class to generate a Pizza object"""

    # Pizza objects and associated cost
    def __init__(self, crust, sauce, cheese, toppings):
        """Initializes a pizza object including the crust, sauce, cheese, toppings, and cost of the pizza
                :param crust: crust type including thin, thick, or gluten free
                :type: str
                :param sauce: sauce type including marinara, pesto, or Liv Sauce
                :type: str
                :param cheese: cheese type including mozerella only
                :type: str
                :param toppings: list of toppings including pineapple, pepperoni, or mushrooms
                :type: list of str"""
        #initialize a pizza
        # set pizza variables
        self.crust = crust
        self.sauce = sauce
        self.cheese = "mozzerella"
        self.toppings = toppings
        # set cost to create
        self.cost = 0
    
    def __str__(self):
        """Returns a string defining all the values of a pizza object
                :returns: string defining a pizza including type of crust, sauce, cheese, toppings, and cost
                :rtype: str
            """
        return("Your pizza has:" + 
               "\n crust: " + self.crust + 
               "\n sauce: " + self.sauce + 
               "\n cheese: " + self.cheese + 
               "\n and" + 
               "\n toppings: " + (", " .join(self.toppings)) +
               "\n cost is: " + str(self.cost))
    
    def total_cost(self):
        """Calculates the cost associated with each type of crust, sauce, and toppings selected
            """
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
