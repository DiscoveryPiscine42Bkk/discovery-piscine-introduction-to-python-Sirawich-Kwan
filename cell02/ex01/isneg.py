number = input("What is your number? : ")
try:
    number = float(number)
    if number > 0:
        print("This number is positive.")
    elif number < 0:
        print("This number is negative.")
    else:
        print("This number is both positive and negative.")
except:
    print("The input isn't number")