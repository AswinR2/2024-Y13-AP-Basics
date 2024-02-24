# ask the user for their name
username = input("What is your name? ")

# ask the user for their favourite number (integer)
fav_num = int(input("What is your favourite number? "))

# Double, halve and square the user's favourite number
double = fav_num * 2
halve = fav_num / 2
square = fav_num * fav_num

# Greet the user
print()
print(f"Hi {username}, your favourite number number is {fav_num}.")
print()
 
# Output the results of doubling, halving and
# sqauring their favourite integer

print(f"Double {fav_num} is {double}.")
print(f"Half {fav_num} is {halve}.")
print(f"{fav_num} sqaured is {square}.")

# Below is how you leave a space
print()

print("Have a nice day.")