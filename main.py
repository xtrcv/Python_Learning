#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_unscrambled = []

letters_to_add = []

for char in range(nr_letters):
  while nr_letters > len(letters_to_add):
    letters_to_add.append(str(random.choice(letters)))
    password_unscrambled.append(letters_to_add)

symbols_to_add = []

for sym in range(nr_symbols):
  while nr_symbols > len(symbols_to_add):
    symbols_to_add.append(str(random.choice(symbols)))
    password_unscrambled.append(symbols_to_add)

numbers_to_add = []

for num in range(nr_numbers):
  while nr_numbers > len(numbers_to_add):
    numbers_to_add.append(str(random.choice(numbers)))
    password_unscrambled.append(numbers_to_add)

def listToString(stringAsList):
  str = ""
  for item in letters_to_add:
    str += item
  for item in symbols_to_add:
    str += item
  for item in numbers_to_add:
    str += item
  return str

new_password_unscrambled = listToString(password_unscrambled)

password_scrambled = []

for char in new_password_unscrambled:
  password_scrambled += random.choice(password_unscrambled)

def listToStringFinal(password_scrambled):
  str = ""
  for item in password_scrambled:
    str += item
  return str

final_password_scrambled = listToStringFinal(password_scrambled)

print(f"Your password is: {final_password_scrambled}")