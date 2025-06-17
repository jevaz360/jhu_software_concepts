import pytest
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

@pytest.mark.order
def test_order_initialize():
    my_order = Order()
    assert my_order.order == []
    assert my_order.cost == 0
    assert my_order.paid == False

@pytest.mark.order
def test_order_str():
    my_order = Order()
    my_pizza = Pizza("thin", "marinara", "mozzerella",["pineapple", "pepperoni"])
    my_order.input_pizza(my_pizza.crust, my_pizza.sauce, my_pizza.cheese, my_pizza.toppings)
    assert my_order.__str__() == ("Your pizza has:" + 
               "\n crust: " + "thin" + 
               "\n sauce: " + "marinara" + 
               "\n cheese: " + "mozzerella" + 
               "\n and" + 
               "\n toppings: " + "pineapple, pepperoni" +
               "\n cost is: " + str(10) +
               "\n total cost is: " + str(10))

@pytest.mark.order
def test_order_input_pizza():
    my_order = Order()
    my_pizza = Pizza("thin", "marinara", "mozzerella",["pineapple", "pepperoni"])
    my_order.input_pizza(my_pizza.crust, my_pizza.sauce, my_pizza.cheese, my_pizza.toppings)
    assert my_order.cost == 10

@pytest.mark.order
def test_order_paid():
    my_order = Order()
    my_order.order_paid()
    assert my_order.paid == True
