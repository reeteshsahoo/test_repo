# write a mutliplication  #
def multiply(a, b):
    return a * b


# write a addition function
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


main = __name__ == "__main__"
if main:
    # Test the multiplication function
    print("Multiplication of 3 and 4:", multiply(3, 4))  # Expected output: 12

    # Test the addition function
    print("Addition of 3 and 4:", add(3, 4))  # Expected output: 7

    a = input("Enter a number: ")
    b = input("Enter another number: ")

    # Convert inputs to integers
    a = int(a)
    b = int(b)
    # Print the results of multiplication and addition
    print("Multiplication of", a, "and", b, ":", multiply(a, b))
 
    #Test the subtraction function
    print("Subtraction of", a, "and", b, ":", subtract(a, b))  # Expected output: a - b