
#tpe hints use of mypy
def meow(n:int)-> str:
        """
        Meow n times

        :param n: number of times to meow
        :type n: int
        :raise TypeError: if n is not an int
        :return: A string of n meows one per line
        :rtype:str

        usage of the docstring 
        """
        return "meow\n"*n


number:int = input("Number: ")
meows: str=meow(number)
print(meows, end="")

#mypy meow_18.py will consider this annotations and says whether there are any Type errors or not 