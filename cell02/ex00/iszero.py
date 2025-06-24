number = input("What is your number? : ")
try:
    number = float(number)
    if number == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
except:
    print("The input isn't number")