# Ask the user for the width and height
#(assume they put in valid data)
width = float(input("Width: "))
Height = float(input("Height: "))

#calculate the area / perimeter
area = width * Height
perimeter = (width + Height) * 2

# Output the area and perimeter

print(f"\nYour area is {area}.")
print(f"Your perimeter is {perimeter}.")