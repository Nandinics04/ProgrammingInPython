students=[
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Darco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"}
]

#usage of list of comprehensions
# griffindor=[
#     student["name"] for student in students if student['house'] == "Gryffindor"
# ]
# print(*griffindor)


# use of filter which can push the wanted words based on the condition
def is_gryffindor(student):
    return student["house"] == "Gryffindor"

gryffindors = filter(lambda s: s['house']=='gryffindor',students)
print(type(gryffindors))
print(*gryffindors)




