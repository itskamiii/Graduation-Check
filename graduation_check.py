## Credit check for graduation
name = input("Enter Student Name: ")
credits = int(input("Enter Credits Completed: "))

if credits >= 120:
    print(name + " is eligible to graduate!")
else:
    remaining = 120 - credits
    print(name + " needs " + str(remaining) + " more credits.")
    
##credit check but with list

student_credits = [125, 98, 112, 130, 85]

for credits in student_credits:
    if credits >= 120:
        print(f"Student with {credits} is eligible to graduate!")
    else:
        remaining = 120 - credits
        print(f"Student with {credits} needs {remaining} more credits.")