name = input("enter your name")
age = input("enter your age")
phone_no = input ("enter your phone_no")
print(name, age, phone_no)


print('''================\nName Of College \n=================''' )
print(''' 1.Add New Student\n 2.Delete Student\n 3.Search Student''')
choice =  int(input("Enter You choice :- "))
if(choice == 1):
    print("Add New Student")
    name = input("Enter Name :- ")
    age = int(input("Enter Age :- "))
    phone_number = int(input("Enter Phone Number :-"))
    print("New Student is added")
elif(choice == 2):
    name = input("Enter Name of Student:- ")
    print("Delete Student")
elif(choice == 3):
    name = input("Enter Name of Student:- ")
    print("It should display student Name",name)
else:
    print("Invalid Choice")