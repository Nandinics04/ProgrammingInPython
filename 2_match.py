#conditionals

#flow chart / control flow

# x=int(input("What's x ? "))
# y=int(input("What's y ? "))

# if x<y:
#   print("x is less than y")
# if x>y:
#   print("x is greater than y")
# else:
#   print("x equals y")

#or operator

# if x>y or x<y:
#   print("x is not equal y")
# else:
#   print("x equals y")

#and operator

# score=int(input("What's the score? "))

# if 90<=score<100:
#   print("grade  A")
# elif 80<=score<90:
#   print("grade B")
# elif 70<=score<80:
#   print("grade C")
# else:
#   print("grade D")


#modulo operator

# if x%2==0:
#   print("even number")
# elif:
#   print("odd number")

# def main():
#   x=int(input("What's x? "))
#   if is_even(x):
#     print("it is even")
#   else:
#     print("it is odd")

# def is_even(x):
#   # return True if x%2 == 0 else False
#   return x%2==0

# main()

#match operator

name=input("what's ur name ? ")

match name:
  case "Harry" | "Herminone" | "Ron":
    print("Grffindor")
  case "Darco":
    print("Slytherin")
  case _:
    print("Who?")
