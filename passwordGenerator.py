import random

print('Password Generator')


chars = "abcdefhijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456790!@#$%^&*()_+"
number = int(input("How many passwords do you want to generate: "))


length =  int(input("The length for each password: "))

print("\n here are your passwords: ")

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)

    print(passwords)

