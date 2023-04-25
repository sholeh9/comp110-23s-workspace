"""Practice instantiating Pizza class"""

from pizza import Pizza

#instead of method calls with (), you use attributes with .variable

my_pizza: Pizza = Pizza ("large", 1, True)
#my_pizza.size = "large"
#my_pizza.toppings = 1
#my_pizza.gluten_free = True

#print(Pizza)
#print(my_pizza)

print(my_pizza.size)
print(my_pizza.gluten_free)

sals_pizza: Pizza = Pizza("small", 2, False)

#def price(pizza_order: Pizza) -> float:
    #"""Calculate and return cost of pizza."""
    #cost: float = 0.0
    #if pizza_order.size == "large":
        #cost = 6.0
    #else:
        #cost = 5.0
    #charge .75 per topping
    #cost += .75 * pizza_order.toppings
    # charge $1 for gluten free
    #if pizza_order.gluten_free:
        #cost += 1.0
    #return cost

#print(sals_pizza.price())

print(my_pizza.toppings)
print(my_pizza.price())
my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())
