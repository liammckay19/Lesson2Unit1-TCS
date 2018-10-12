import sys
import io
def main():
    # celsius to Fahrenheit conversion (input = celsius, output = Fahrenheit)

    # Pseudocode:
    # 1. Get input from the user in degrees celsius
    # 2. Calculate fahrenheit from user input
    # 3. print result to user

    # even better
    # 1. get input from the user
    # 2. evaluate input as a number
    # 3. save number into a variable
    # 4. calculate F with formula
    # 5. save the F variable
    # 6. print message explaining the calculation
    # 7. print the F variable

    celsius = eval(input("Enter a temp in degrees Celsius: "))
    fahrenheit = 9 / 5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()