
list_of_numbers = list(range(1, 11))

powers_of_two = list(map((lambda n : 2 ** n), list_of_numbers))

print(powers_of_two)