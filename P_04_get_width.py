# Ask user for widht and loop untill they enter a number that is more than zero

error = "Please enter a number that is more than zero\n"
while True:

    try:
        # asking for input
        width = float(input("Width: "))

        # checking that the num is > 0
        if width > 0:
            break
        else:
            print("error")

    except ValueError:
        print(error)