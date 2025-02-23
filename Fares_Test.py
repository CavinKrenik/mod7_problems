def ferry_fare(age, vehicle):
    if age <= 18:
        return "Child: FREE"
    elif 19 <= age <= 64:
        return f"Adult with Vehicle: $20" if vehicle else f"Adult without Vehicle: $10"
    else:  # age 65+
        return f"Senior with Vehicle: $15" if vehicle else f"Senior without Vehicle: $5"

ages = [10, 30, 70]

for age in ages:
    if age <= 18:
        print("Child: FREE")
    else:
        print("Select fare type: 1. Adult without Vehicle, 2. Adult with Vehicle, 3. Senior without Vehicle, 4. Senior with Vehicle")
        fare_type = int(input())
        if fare_type == 1:
            print(ferry_fare(age, False))
        elif fare_type == 2:
            print(ferry_fare(age, True))
        elif fare_type == 3:
            print(ferry_fare(age, False))
        elif fare_type == 4:
            print(ferry_fare(age, True))
