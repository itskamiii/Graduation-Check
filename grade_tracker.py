def calculate_average(scores):
    """Calculates the average of a list of numbers."""
    if not scores:
        return 0
    return sum(scores) / len(scores)

def get_letter_grade(average):
    """Converts a numerical average into a letter grade."""
    if average >= 90: return "A"
    if average >= 80: return "B"
    if average >= 70: return "C"
    if average >= 60: return "D"
    return "F"

#main dictionary to store our data
classroom = {}

print("--- Welcome to the Dean's Desk Student Tracker ---")

while True:
    name = input("\nEnter student name (or type 'quit' to finish): ").strip()
    
    if name.lower() == 'quit':
        break
    
    try:
        #get scores as a string, split them by commas, and convert to integers
        raw_scores = input(f"Enter scores for {name} separated by commas (e.g., 85, 90, 78): ")
        scores_list = [int(s.strip()) for s in raw_scores.split(",")]
        
        #store in our dictionary
        classroom[name] = scores_list
        print(f"✅ Data saved for {name}.")
        
    except ValueError:
        print("❌ Error: Please enter numbers only, separated by commas.")

#the final step is to generate the report and save to a file
print("\n--- Generating Final Report ---")

#using 'with open' is the best practice for file input and output
with open("class_report.txt", "w") as file:
    file.write("STUDENT GRADE REPORT\n")
    file.write("====================\n")
    
    for name, scores in classroom.items():
        avg = calculate_average(scores)
        grade = get_letter_grade(avg)
        
        report_line = f"{name}: Average = {avg:.2f} | Grade = {grade}"
        print(report_line)#shows it in terminal
        file.write(report_line + "\n")#saves to file

print("\n Report saved to 'class_report.txt'!")