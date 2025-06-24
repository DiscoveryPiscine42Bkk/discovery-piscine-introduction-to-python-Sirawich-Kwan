first_number = input("Enter the first number:\n")
second_number = input("Enter the second number:\n")
try:
    first_number = int(first_number)
    second_number = int(second_number)
except:
    print("The input isn't number!")
    exit()

total = first_number * second_number
print(f"{first_number} x {second_number} = {total}")
if total > 0:
    print("This result is positive.")
elif total < 0:
    print("This result is negative.")
else:
    print("This result is both positive and negative.")