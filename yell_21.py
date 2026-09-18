def main():
    yell("This", "is", 'CS50',"course")

# def yell(*words):
#     uppercased=[]
#     for word in words:
#         uppercased.append(word.upper())

#     print(*uppercased)


#usage of map
# def yell(*words):
#     uppercased=map(str.upper,words)   #map function iterates over each word in words and pass this upper method and returns as uppercase 
#     print(*uppercased)


#use of list comprehensions
def yell(*words):
    uppercased=[word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()