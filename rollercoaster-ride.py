print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

price = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What's your age? "))
    if age < 12:
        price = 5
        print("Child tickets are $5.")
    elif age <= 18:
        price = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        price = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want photos? Y or N: ")
    if wants_photo.upper() == "Y":
        price += 3

    print(f"The total bill is ${price}")

else:
    print("Sorry, you have to grow taller before you can ride")
