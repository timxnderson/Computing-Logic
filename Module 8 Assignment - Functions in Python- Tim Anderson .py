# Define the function greaterThan
def greaterThan(x, y):
    if x > y:
        return True
    else:
        return False

# Main section of the program
if __name__ == "__main__":
    # Assign values
    a = 2
    b = 3
    
    # Call the function
    result = greaterThan(a, b)
    
    # Print the output statement
    print(f"The statement {str(a)} is greater than {str(b)} is {str(result)}")
    
    # Test scenario with a = 10 and b = 6
    a = 10
    b = 6
    result = greaterThan(a, b)
    print(f"The statement {str(a)} is greater than {str(b)} is {str(result)}")
