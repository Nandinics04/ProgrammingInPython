# lists

# students= ["hermione", "Ron", "Harry"]

# for student in students:
#   print(student);

# for i in range(len(students)):
#   print(students[i])

# students={
#     "Hermione": "Griffindor",
#     "Harry":"Griffindor",
#     "Rohn":"Griffindor"
# }

# for student in students:
#   print(student, students[student], sep=", ")


students = [
  {"name": "Hermione", "house": "Griffindor", "patronus": "Otter"},
  {"name": "Ron", "house": "Griffindor", "patronus": "Stag"},
  {"name": "Harry","house":"Griffindor", "patronus": "Jack Russel terreier"},
  {"name": "Darcon", "house":"Slitterin", "patronus":None}

]
for student in students:
  print(student["name"], student["house"],student["patronus"],sep=",")

for i in range(3):
  for j in range(3):
    print("#", end="")
  print()

  