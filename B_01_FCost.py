# Ask user for width, height and cost loop untill they enter a number that is more than zero

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
    # Get width, height and cost/m
    width = num_check("Width(in m): ")
    height = num_check("Height(in m): ")
    costoff = num_check("Cost(/m): ")

    # Calculate perimeter and Total cost
    tcost = (width * height) * costoff
    perimeter = (width + height) * 2

    # Display output
    print(f"\nYour perimeter is {perimeter}m.")
    print(f"Your total cost is {tcost}$.")

    # Ask user if they want to keep going
    keep_going = input("Press enter keep going or any key to quit. ")
    print()

print("Thank you for using the Fence price calculator")