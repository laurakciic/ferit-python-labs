name = input("Unesi ime: ")
age = int(input("Unesi starost: "))
repeat = int(input("Koliko ponavljanja: "))

result = 100 - age + 2021

for x in range (repeat):
    print("bok " + name + ", imat ces 100 godina " + str(result) + ". godine, predobro")
