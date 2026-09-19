full_name = input("Enter your name and surname: ").strip().split()
group = input("Enter group (AB-12): ").strip().upper()

name_check = len(full_name) == 2 and full_name[0].isalpha() and full_name[1].isalpha()

length = len(group) == 5
dash = length and group[2] == "-"
alpha = length and group[:2].isalpha()
digit = length and group[3:].isdigit()

if name_check and length and dash and alpha and digit:
    first = full_name[0].title()
    second = full_name[1].title()
    init = first[0] + "." + second[0] + "."
    print(f"{second}, {first} - {group} {init}")
elif not name_check:
    print("Error: incorrect name or surname")
elif not length:
    print("Incorrect length | example: >>AB-12<<")
elif not dash:
    print("There is no dash between | example: AB-12")
elif not alpha:
    print("There are no letters | example: >>AB-12") 
elif not digit:
    print("There are no numbers | example: AB-12<<")   