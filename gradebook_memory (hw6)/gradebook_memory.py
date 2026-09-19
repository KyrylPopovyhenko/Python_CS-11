students = [
    {"name": "Andrew", "group": "CS-55", "scores": [76, 65, 80, 90]},
    {"name": "Mary", "group": "MR-23", "scores": [60, 56, 66, 75]},
    {"name": "Peter", "group": "CS-56", "scores": [72, 65, 76, 56]},
    {"name": "Robert", "group": "CS-55", "scores": [95, 92, 96, 91]},
    {"name": "John", "group": "MR-23", "scores": []}
]

group = set()
group_found = False
id_check = ()

for student_counter, student in enumerate(students, start=1):
    student["id"] = (student["group"], student_counter)
    # ids = list(range(1, len(students) + 1))

print("\n___Average scores___\n")

for student in students:
    group.add(student["group"])
    
    if student["scores"]:
        average_score = sum(student["scores"]) / len(student["scores"])
        print(f"{student.get("name")}'s average score: ", average_score) 
    else:
        print(f"{student.get("name")} has no scores")

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
            print(student["id"])
            group_found = True    

    if not group_found:
        print("Group not found")

else:
    print("Incorrect group data example(AB-12)")

if group_found:
    id_entered = int(input("Enter student ID: "))
    id_check = (group_entered, id_entered)
    for student in students:
        if id_check == student["id"]:
            print("\n___Student found___\n")
            print(student["name"], student["id"])
            break
    else:
        print("Student is not found")

# for student in students:
#     if student["id"] == id_entered:
#         print(student["name"])
#         break
# else:
#         print("Student not found")