name = input("Enter Student Name: ")
credits = int(input("Enter Credits Completed: "))

if credits >= 120:
    print(name + " is eligible to graduate!")
else:
    remaining = 120 - credits
    print(name + " needs " + str(remaining) + " more credits.")