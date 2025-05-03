'''This is a program to find the
current number of flights in an airport'''
landings_count=356
takeoffs_count=245
initial_flights=89
current_flights = initial_flights + landings_count - takeoffs_count
#Displaying the current number of flights
print("Current number of flights:",current_flights)
