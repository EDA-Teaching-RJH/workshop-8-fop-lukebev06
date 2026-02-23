import re

student_id = input("enter a valid student id: ")
#begins 4 letters. ends 4 numbers
id_format = r"^\w{4}\d{4}$"

if re.search(id_format,student_id):
    print("valid student id")

else:
    if len(student_id) != 8:
        print("invalid length")

    elif not student_id[ :4].isalpha():
        print("the first part of the id isnt all characters")

    elif not student_id[4:].isdigit():
        print("the last 4 characters werent digits")
