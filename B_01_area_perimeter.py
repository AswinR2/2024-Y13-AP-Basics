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

# Main Routine starts here...
            
keep_going = ""
while keep_going == "":
    # Get width and height
    width = num_check("Width: ")
    height = num_check("Height: ")

    # Calculate area / perimeter
    area = width * height
    perimeter = (width + height) * 2

    # Display output
    print(f"\nYour area is {area}.")
    print(f"Your perimeter is {perimeter}.")

    # Ask user if they want to keep going
    keep_going = input("Press enter keep going or any key to quit. ")
    print()

print("Thank you for using the area / perimeter calculator")