# test.py - Sample Python Script

def greet_user(name):
    """Greet the user by name."""
    print(f"Hello, {name}! Welcome to the Python script.")

def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

def print_even_numbers(limit):
    """Print all even numbers up to a certain limit."""
    print(f"Even numbers up to {limit}:")
    for i in range(1, limit + 1):
        if is_even(i):
            print(i, end=' ')
    print()

def main():
    """Main function to run the script."""
    name = input("Enter your name: ")
    greet_user(name)

    try:
        limit = int(input("Enter a number: "))
        print_even_numbers(limit)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
    def main():
    """Main function to run the script."""
    name = input("Enter your name: updated1 ")
    greet_user(name)

    try:
        limit = int(input("Enter a number: "))
        print_even_numbers(limit)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":updated
    main()

