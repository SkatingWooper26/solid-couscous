
def mileToKilometer(miles):
    kilometers = miles * 1.60934
    return kilometers

def kilometerToMile(kilometers):
    miles = kilometers / 1.60934
    return miles

choice = input("Do you want to convert MILES or KILOMETERS?: ").strip().lower()

if choice == "miles":
    miles = float(input("Enter the distance in miles: "))
    kilometers = mileToKilometer(miles)
    print(f"{miles} miles is equal to {kilometers:.2f} kilometers")
else:
    kilometers = float(input("Enter the distance in kilometers: "))
    miles = kilometerToMile(kilometers)
    print(f"{kilometers} kilometers is equal to {miles:.2f} miles")