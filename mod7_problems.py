'''
#1. Write a function called count_vowels(input) that takes a string
and returns the number of vowels (a, e, i, o, u) in it.
'''

def count_vowels(input):
    vowels = ('a', 'e', 'i', 'o', 'u')
    count = 0
    for char in input.lower():
        if char in vowels:
            count += 1
    return count

'''
#2. Write a function called is_palindrome(s) that checks whether a string is a
palindrome
(reads the same forward and backward, ignoring case). The function should
returns
either True or False.
'''

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

'''
#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
For example, water is very effective to fight fire.
Write a function called type_advantage(attacker, defender) that takes two
Pokémon types as
strings and returns "Super Effective", "Not Very Effective", or "Neutral" based
on
simple type effectiveness rules. Your solution only needs to work for these
three sets of input:
print(type_advantage("Water", "Fire")) # "Super Effective"
print(type_advantage("Fire", "Water")) # "Not Very Effective"
print(type_advantage("Electric", "Grass")) # "Neutral"
'''

def type_advantage(attacker, defender):
    if attacker == "Water" and defender == "Fire":
        return "Super Effective"
    elif attacker == "Fire" and defender == "Water":
        return "Not Very Effective"
    elif attacker == "Electric" and defender == "Grass":
        return "Neutral"
    return "Neutral"

'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington
State Ferry fare
based on age and whether the person has a vehicle. Assume the following rates:
* Adults (19-64): $10 without a vehicle, $20 with a vehicle.
* Seniors (65+): $5 without a vehicle, $15 with a vehicle.
* Children (0-18): Free.
'''

def ferry_fare(age, vehicle):
    if age <= 18:
        return 0
    elif 19 <= age <= 64:
        return 20 if vehicle else 10
    else:  # age 65+
        return 15 if vehicle else 5

'''
#5. Write a function called level_up(experience) that takes a player's experience
points
and returns their new level based on these rules:
* 0-99 XP → Level 1
* 100-199 XP → Level 2
* 200+ XP → Level 3
'''

def level_up(experience):
    if experience < 100:
        return 1
    elif experience < 200:
        return 2
    else:
        return 3
