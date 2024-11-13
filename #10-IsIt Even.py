#10-IsItEven?

# Function that checks if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# Main function
def main():
    # Ask the user to input a number
    number = int(input("Enter a number: "))
    
    # Pass the number to the function and get the result
    result = check_even_odd(number)
    
    # Print the result
    print(result)

# Call the main function
if __name__ == "__main__":
    main()
