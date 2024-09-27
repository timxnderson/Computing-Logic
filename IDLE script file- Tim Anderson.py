# Define the list of numbers from 1 to 15
numbers = list(range(1, 16))

# Loop through each number in the list
for number in numbers:
    # Check if the number is even
    if number % 2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")
