
# all around print in pyhton

name=input("what is your name ? ")
#discussed of parameters, optimal parameters
print("My name is " + name)
print("My name is", name)
print("My name is ", end="")
print(name)
print("My name is", name,sep='???')
print('Hey "friend" ')
print("Hey \"friend\" ")
print(f"Hello, {name}") # format string or f string

#string
name=name.strip() # remove the white spaces from left and right
name=name.capitalize() # used to capitalise the first char of the input
name=name.title() # capitalize of each char of first word

print(name)

hobby=input("what are your one single hobby ? ")

#instead we do
hobby=hobby.strip().title()
print("hobbies", hobby)

first,last=name.split(" ")
print(f"So first name is {first}")

#interactive mode is when i type pyhton on terminal







