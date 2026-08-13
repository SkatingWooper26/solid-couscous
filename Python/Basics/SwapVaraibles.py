
def SwapVariables(a, b):
    return b, a

a = input("enter the first variable: ")
b = input("enter the second variable: ")
a, b = SwapVariables(a, b)
print("After swapping:")
print("First variable:", a)
print("Second variable:", b)