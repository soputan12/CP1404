from unreliable_car import UnreliableCar

car1 = UnreliableCar("Good", 100, 75)
car2 = UnreliableCar("Bad", 100, 5)

for i in range(1, 12):
    print(f"Trying to drive {i} km")
    print(f"{car1.name} drove {car1.drive(i)} km")
    print(f"{car2.name} drove {car2.drive(i)} km")

print(car1)
print(car2)