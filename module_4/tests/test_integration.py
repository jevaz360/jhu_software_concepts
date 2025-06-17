class Pizza:
    # Pizza objects and associated cost
    def __init__(self, crust, sauce, cheese, toppings):
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
        
class Order:
    def __init__(self):
        #Initialize a customer order
        self.order = []
        #Initialize a customer cost
        self.cost = 0
        #Initialize a payment status
        self.paid = False

    def __str__(self):
       for value in self.order:
           return value.__str__() + "\n total cost is: " + str(self.cost)

    
    def input_pizza(self, crust, sauce, cheese, toppings):
        #Input customer's order for a given pizza
        #Initialize the pizza object and attach to the order
        pizza = Pizza(crust, sauce, cheese, toppings)
        self.order.append(pizza)
        #Update the cost
        pizza.total_cost()
        self.cost += pizza.cost

    def order_paid(self):
        # Set order as paid once payment has been collected
        self.paid = True

def test_integration():
    # Initialize order
    my_Order = Order()

    # create test pizza case 1
    my_pizza = Pizza("thin", "marinara", "mozzerella",["pineapple", "pepperoni"])
    my_pizza.total_cost()

    # input pizza case 1 to order
    my_Order.input_pizza(my_pizza.crust, my_pizza.sauce, my_pizza.cheese, my_pizza.toppings)

    # create test pizza case 2
    my_pizza_2 = Pizza("thin", "Liv Sauce", "mozzerella",["pineapple", "mushrooms"])
    my_pizza_2.total_cost()

    # input pizza case 2 to order
    my_Order.input_pizza(my_pizza_2.crust, my_pizza_2.sauce, my_pizza_2.cheese, my_pizza_2.toppings)

    # assert that the total cost of the order is greater than the individual pizza cost
    assert my_pizza.cost < my_Order.cost
    assert my_pizza_2.cost < my_Order.cost
    
    # assert that the individual pizza costs add up to the total order cost
    assert my_Order.cost == my_pizza.cost + my_pizza_2.cost


