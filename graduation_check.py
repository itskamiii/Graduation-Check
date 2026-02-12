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
        
##credit check with dictionary
student_data = {
    "Jandell": 125,
    "Alex": 98,
    "Sam": 112,
    "Jordan": 130,
    "Riley": 85
}

#we sort by credits (the values) in descending order
sorted_students = sorted(student_data.items(), key=lambda item: item[1], reverse=True)

for name, credits in sorted_students:
    if credits >= 120:
        print(f"{name}: Ready to Graduate with {credits} credits.")
    else:
        print(f"{name}: Needs {120 - credits} more credits.")