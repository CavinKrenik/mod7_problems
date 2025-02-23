def ferry_fare(age, vehicle):
    if age <= 18:
        return "Child: FREE"
    elif 19 <= age <= 64:
        return f"Adult with Vehicle: $20" if vehicle else f"Adult without Vehicle: $10"
    else:  # age 65+
        return f"Senior with Vehicle: $15" if vehicle else f"Senior without Vehicle: $5"

def calculate_total_fare(adults, seniors, vehicle):
    total_fare = 0
    for _ in range(adults):
        total_fare += 20 if vehicle else 10
    for _ in range(seniors):
        total_fare += 15 if vehicle else 5
    return total_fare

ages = [10, 30, 70]

for age in ages:
    if age <= 18:
        print("Child: FREE")
    else:
        print("Enter the number of adults:")
        adults = int(input())
        print("Enter the number of seniors:")
        seniors = int(input())
        print("Do they have a vehicle? (yes/no)")
        vehicle = input().lower() == 'yes'
        total_fare = calculate_total_fare(adults, seniors, vehicle)
        print(f"Total fare: ${total_fare}")
