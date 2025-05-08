# Take user input and convert it to an integer
num = int(input("Enter a number: "))

# Check if the number is divisible by 2 (even)
if num % 2 == 0:
    print(num, "is an even number")
else:
    # If not divisible by 2, it's odd
    print(num, "is an odd number")