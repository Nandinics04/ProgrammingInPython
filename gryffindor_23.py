
#usage of dictionary comprehension
students=["Hermione", "Harry", "Ron"]

# gryffindors=[{"name": student, "house":"Gryffindor"} for student in students]
# griffindor={student:"Gryffindor" for student in students}
# print(griffindor)

# for i in range(len(students)):
#     print(i+1, students[i])


#usage of enumerate -> adding ranking to the system

for i, student in enumerate(students):
    print(i+1, student)