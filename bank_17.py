#usage of global variable
#global variable is not used to write and update the value in it. it can only access to read that varaible
#use of global keyword

# balance=100

# def main():
#     print('Balance: ',balance)
#     deposite(100)
#     withdraw(50)
#     print('Balance: ', balance)

# def deposite(n):
#     global balance
#     balance+=n

# def withdraw(n):
#     global balance
#     balance-=n

# if __name__ == "__main__":
#     main()








#usage of class, and objects

class Account:
    def __init__(self):
        self._balance=0

    @property
    def balance(self):
        return self._balance

    def deposite(self,n):
        self._balance+=n
    def withdraw(self,n):
        self._balance-=n

def main():
    account=Account()
    print("Balance: ",account.balance)
    account.deposite(100)
    account.withdraw(20)
    print("Balance: ",account.balance)
    account._balance=5000
    print("Balance: ",account.balance)


if __name__ == "__main__":
    main()

