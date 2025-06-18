Name: Janice Vaz JHED ID: jvaz3

Module 4: Pytest and Sphinx

Approach: In this assignment, we were tasked with writing a Pizza ordering application comprising two class objects. One class object being the Pizza, and the other class object being an Order which may hold/keep track of multiple Pizzas. These are organized into the pizza.py and order.py files respectively. Most important of the functions for each object class was the cost of an individual pizza, and the total cost of the order. To ensure the integrity of the files, a test_pizza.py file was made, and using pytest, tested the specific case where someone may order a pizza with a thin crust, marinara sauce, and pineapple and pepperoni toppings. The expected initialization of the pizza, the cost of the pizza, and the expected string output (string statement describing what was the pizza made of and what the cost of the pizza was) were tested against asserted known/expected values. Similarly, the order.py file was tested with a test_order ensuring the order was initialized properly. Lastly, an integration test was used to see if an order would properly hold more than one pizza while retaining the true value of the total cost. Sphinx and Read the Docs was used to create documentation for the classes/functions.

Known Bugs:

- Was unable to import order.py/pizza.py into test files so I had to copy over the code from the original files. Ideally, a working import would be better.
- **init** and **str** functions were ignored for some reason when using sphinx/read the docs
