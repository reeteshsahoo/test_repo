# write a mutliplication  #
def multiply(a, b):
    return a * b


# write a addition function
def add(a, b):
    return a + b


main = __name__ == "__main__"
if main:
    # Test the multiplication function
    print("Multiplication of 3 and 4:", multiply(3, 4))  # Expected output: 12

    # Test the addition function
    print("Addition of 3 and 4:", add(3, 4))  # Expected output: 7

    a = input("Enter a number: ")
    b = input("Enter another number: ")
