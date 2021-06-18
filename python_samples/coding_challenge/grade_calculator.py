'''
Given different scored marks of students, we need to find grades.
The test score is an average of the respective marks scored in assignments, tests and lab-works.
The final test score is assigned using below formula.
    10 % of marks scored from submission of Assignments
    70 % of marks scored from Test
    20 % of marks scored in Lab-Works
Grade will be calculated according to :
    1. score >= 90 : "A"
    2. score >= 80 : "B"
    3. score >= 70 : "C"
    4. score >= 60 : "D"
    5. Score < 60: "E"
Also, calculate the total class average and letter grade of class.
'''

def calculate_average(marks):
    return float(sum(marks))/len(marks)

def calculate_total_average(student):
    assignments = calculate_average(student['assignment'])
    test = calculate_average(student['test'])
    lab = calculate_average(student['lab'])
    return (0.1 * assignments + 0.7 * test + 0.2 * lab)

def calculate_grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "E"

def calculate_total_class_average(students):
    results = list()
    for student in students:
        student_avg = calculate_total_average(students[student])
        student_grd = calculate_grade(student_avg)
        print(f"{'':=<80}\nAverage marks of {students[student]['name']} is : {student_avg}")
        print(f"Grade of {students[student]['name']} is : {student_grd}")
        results.append(student_avg)
    return calculate_average(results)

students = dict(jack = { "name" : "Jack Frost", 
            "assignment" : [80, 50, 40, 20], 
            "test" : [75, 75], 
            "lab" : [78.20, 77.20] },
james = { "name" : "James Potter", 
            "assignment" : [82, 56, 44, 30], 
            "test" : [80, 80], 
            "lab" : [67.90, 78.72] },
dylan = { "name" : "Dylan Rhodes", 
            "assignment" : [77, 82, 23, 39], 
            "test" : [78, 77], 
            "lab" : [80, 80] },
jess = { "name" : "Jessica Stone", 
            "assignment" : [67, 55, 77, 21], 
            "test" : [40, 50], 
            "lab" : [69, 44.56] },
tom = { "name" : "Tom Hanks", 
            "assignment" : [29, 89, 60, 56], 
            "test" : [65, 56], 
            "lab" : [50, 40.6] })

# Calculate the average of whole class
class_avg = calculate_total_class_average(students)
class_grd = calculate_grade(class_avg)
print(f"\n{'':*<80}\nAverage marks of class is : {class_avg}")
print(f"Grade of class is : {class_grd}\n{'':*<80}")
