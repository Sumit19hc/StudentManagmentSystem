def CreateRegister():
    file = open("studentinfo.txt", "a+")
    return file

def WriteToRegister(f, name, age, mob_number):
    f.write("{}|{}|{}\n".format(name, age, mob_number))
    f.close()

def ReadRegister():
    n = open("studentinfo.txt")
    print(n.read())


def header():
    print('''------------------------ \n  G. M. C. Chindwara.. \n------------------------''')


def add(f):
    print("Add New Student")
    name = input("Enter Name :- ")
    age = int(input("Enter Age :- "))
    mob_number = int(input("Enter mob_number :- "))
    WriteToRegister(f, name, age, mob_number)
    print("New Student is added")


#
# def delete():
#     name = input("Enter Name of Student:- ")
#     print("Delete Student")


# def search():
#     name = input("Enter Name of Student:- ")
#     print("It should display student Name", name)


def choice():
    print(''' 1.Add New Student\n 2.Delete Student\n 3.Search Student''')
    choice = int(input("Enter You choice :- "))
    return choice


if _name_ == "_main_":
    f = CreateRegister()
    ch = choice()
    if ch == 1:
        header()
        add(f)
        ReadRegister()
    elif ch == 2:
        # header()
        # delete()
    elif ch == 3:
        # header()
        # search()
    else:
        print("Invalid Choice")