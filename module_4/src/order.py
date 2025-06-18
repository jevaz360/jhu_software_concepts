"""This module is to create an order with pizza objects created 
where the order calculates the total cost given multiple pizzas"""
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
        
class Order:
    """This is a class to generate an Order object"""
    def __init__(self):
        """Initializes an Order object to include an empty order list, a cost set to 0, and a payment status as false
            """
        #Initialize a customer order
        self.order = []
        #Initialize a customer cost
        self.cost = 0
        #Initialize a payment status
        self.paid = False

    def __str__(self):
       """Returns a string defining all pizza objects within an order

                :returns: string defining each pizza in the order, including each pizza's type of 
                crust, sauce, cheese, toppings, and cost as well as the total cost of the order
                :rtype: str
            """
       for value in self.order:
           return value.__str__() + "\n total cost is: " + str(self.cost)

    
    def input_pizza(self, crust, sauce, cheese, toppings):
        """Creates a pizza object including the crust, sauce, cheese, toppings, and cost of the pizza. Appends the pizza to the order, and updates the total cost of the order.
                
                :param crust: crust type including thin, thick, or gluten free
                :type: str
                :param sauce: sauce type including marinara, pesto, or Liv Sauce
                :type: str
                :param cheese: cheese type including mozerella only
                :type: str
                :param toppings: list of toppings including pineapple, pepperoni, or mushrooms
                :type: list of str
            """
        #Input customer's order for a given pizza
        #Initialize the pizza object and attach to the order
        pizza = Pizza(crust, sauce, cheese, toppings)
        self.order.append(pizza)
        #Update the cost
        pizza.total_cost()
        self.cost += pizza.cost

    def order_paid(self):
        """Changes the order payment status to True"""
        # Set order as paid once payment has been collected
        self.paid = True

