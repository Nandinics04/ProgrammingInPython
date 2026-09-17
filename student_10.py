#usage of tuple 
class Student:
    def __init__(self,name,house,patronus):
        self.name=name
        self.house=house
        self.patronus=patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
        

def main():
    student=get_student()
    print(student)



def get_student():
    name=input("Name: ")
    house=input("House: ")
    patronus=input("Patronus: ")
    student=Student(name,house,patronus)
    print("Expecto Patronum")
    print(student.charm)
    
    return student

if __name__ == '__main__':
    main()