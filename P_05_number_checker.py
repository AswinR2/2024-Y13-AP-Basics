# Ask user for widht and loop untill they enter a number that is more than zero

def num_check (question):


    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # asking for input
            response = float(input(question))

            # checking that the num is > 0
            if width > 0:
                return response
            else:
                print("error")

        except ValueError:
            print(error)

# Main Routine Goes Here
for item in range(0, 2):
    width = num_check("Width: ")
    print(width)

print()

for item in range(0, 2):
    height = num_check("Height: ")
    print(height)

