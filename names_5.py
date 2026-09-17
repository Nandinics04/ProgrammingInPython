# name=input("What's your name? ")

# with open("names.txt","a") as file:
#     file.write(f"{name}\n")
# file.close()



# with open("names.txt", "r") as file:
#     lines=file.readlines()

# for line in lines:
#     print(line.rstrip())


# with open("names.txt","r") as file:
#     for line in file:
#         print(f"hello, {line.rstrip()}")

names=[]
with open("names_5.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names,reverse=True):
    print(f"Hello, {name}")

with open("names_5.txt") as file:
    for line in sorted(file):
        print("hello,",line.rstrip())
