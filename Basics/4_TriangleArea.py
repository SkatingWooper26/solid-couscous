def triangleArea(base, height):
    return 0.5 * base * height

unit = input("Enter the unit of measurement: ")
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area  = triangleArea(base, height)

print(f"The area of the triangle is: {area} {unit}²")
