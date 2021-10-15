#! /usr/bin/env python3

# print a header and title
print("="*38)
print("Temperature Converter\n")

# create a variable that will determine if the program is repeated, and another that determines user choice of temp conversion
repeat = 1
choice = 0

# outer while loop controls whether program repeats or not, 1 repeats and all other inputs exit
while repeat == 1:

    # inner loop ensures user choice is valid
    while choice < 1 or choice > 2:
        print("1. Celsius to Fahrenheit")
        print("2. Fahernheit to Celsius")
        choice = int(input("Select option: "))

    # get temperature to be converted
    temp = float(input("Enter temperature: "))

    # convert the temperature using the conversion specified by the user
    if choice == 1:
        tempOut = temp * 9 / 5 + 32
        print(f"{temp} degrees C is equal to {tempOut:.2f} degrees F.")
    else:
        tempOut = (temp - 32) * 5 / 9
        print(f"{temp} degrees F is equal to {tempOut:.2f} degrees C.")
    
    # ask if the user wants to convert more temperatures
    print("1. Calculate another")
    print("   Any other input to exit")
    repeat = int(input("Select option: "))

    # reset choice to 0 to ensure user can select which conversion they want
    choice = 0

print("Goodbye!")