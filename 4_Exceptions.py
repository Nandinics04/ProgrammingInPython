#Exceptions
#using try catch statements

def main():
  x=get_number("what is x? ")
  print(f"x is {x}")

def get_number(prompt):
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      pass


main()