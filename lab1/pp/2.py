# Ask the user for a number. 
# Depending on whether the number is even or odd, 
# print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?

num = int(input("Unesi broj: "))
if num % 2 == 0:
    print("Paran")
else:
    print("njeparan")