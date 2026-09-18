
#usage of generators, yeid, iterator
def main():
    n=int(input("What's n? "))
    
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑"*i    #it just generating one row of sheep at a time 


if __name__ == "__main__":
    main()
