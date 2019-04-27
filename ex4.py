#these create variables that we can input into our program
# amount of cars
cars = 100
# how much space is in each car
space_in_a_car = 4.0
# how many drivers are available
drivers = 30
#how many passengers need to be transported
passengers = 90
# cars without drivers, total cars - drivers
cars_not_driven = cars - drivers
# amount of cars that can be driven
cars_driven = drivers
# the amount of cars driven times the space in each car
carpool_capacity = cars_driven * space_in_a_car
# average of passengers per car
average_passengers_per_car = passengers / cars_driven

# prints amount of cars
print("There are", cars, "cars available.")
# prints amount of drivers
print("There are only", drivers, "drivers available.")
# prints the amount of empty cars
print("There will be", cars_not_driven, "empty cars today.")
# prints amount of available seats we have (cars * seats per car)
print("We can transport", carpool_capacity, "people today.")
# prints amount of passengers to transport
print("We have", passengers, "to carpool today.")
# prints amount of passenger needed to be put in each car (passengers / driven cars)
print("We need to put about", average_passengers_per_car, "in each car.")
