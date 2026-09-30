students = [
    {"name": "Andrew", "group": "CS-55", "scores": [76, 65, 80, 90]},
    {"name": "Mary", "group": "MR-23", "scores": [60, 56, 66, 75]},
    {"name": "Peter", "group": "CS-56", "scores": [76, 65, 76, 56]},
    {"name": "Robert", "group": "CS-55", "scores": [95, 92, 96, 91]},
    {"name": "John", "group": "MR-23", "scores": []},
    {"name": "Mary", "group": "CS-56", "scores": [90, 89, 90, 76]}
]

group = set()
student_by_id = {}
group_found = False
id_check = ()

for student_counter, student in enumerate(students, start=1):
    if student_counter == 2:
            continue
    student["id"] = (student["group"], student_counter)
    # ids = list(range(1, len(students) + 1))

for student in students:
    student_id = student.get("id")

    if student_id is not None:
        student_by_id[student_id] = student

max_average = 0
best_student = None

print("\n___Average scores___\n")

for student in students:
    group.add(student["group"])
    
    if student["scores"]:
        average_score = sum(student["scores"]) / len(student["scores"])
        print(f"{student.get("name")}'s average score: ", average_score)
        if average_score > max_average:
            max_average = average_score
            best_student = student
    else:
        print(f"{student.get("name")} has no scores")

if best_student:
    print(f"\nBest result: {best_student["name"]} - {max_average}")

print("\n___List copy___\n")

for student in students:
    copy_scores = student["scores"].copy()
    student["scores"] = [0, 0, 0, 0]
    print(f"{student["scores"], copy_scores}")

print("\n___Student groups___\n")
print(f"Groups: {sorted(group)}")

group_entered = (input("Enter Group: ").upper()) 
group_check = len(group_entered)==5 and group_entered[2]=="-" and group_entered[:2].isalpha() and group_entered[3:].isdigit()

if group_check:
    print("\n___Students ID in this group___\n")
    for student in students:
        if student["group"] == group_entered:
            group_found = True
            student_id = student.get("id")
            if student_id is not None:
                print(student["name"], student["id"])
            else:
                print(f"{student.get("name")} has no ID")   

    if not group_found:
        print("Group not found")

else:
    print("Incorrect group data example(AB-12)")

if group_found:
    id_entered = int(input("Enter student ID: "))
    id_check = (group_entered, id_entered)

    student = student_by_id.get(id_check)

    if student is not None:
        print("\n___Student found___\n")
        print(student["name"], student["id"])
    else:
        print("Student is not found")