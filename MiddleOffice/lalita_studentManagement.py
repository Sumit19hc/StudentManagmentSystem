def CreateRegister():
    file = open("DataBase.txt", "a")
    return file

def AddToRegister(file, name, age, phoneNumber):
    # Write Data to file
    file.write("{}|{}|{}\n".format(name, age, phoneNumber))


def CheckIfStudentExists(file, newStudentName):
    readFile = open("DataBase.txt", "rt")
    data = readFile.readlines()
    for line in data:
        # print("this is line{}".format(line))
        splitData = line.split("|")
        name = splitData[0]
        age = splitData[1]
        phoneNumber = splitData[2]
        if (newStudentName == name):
            print("Student={} already exists".format(newStudentName))
            return True


def Add(file):
    name = input("Enter Name :- ")
    check=CheckIfStudentExists(file,name)
    if check is True:
        print("student already exit ")
        return False
    else:
        age = input("Enter the age:")
        phoneNumber = input("Enter the phone number:")
        AddToRegister(file, name, age, phoneNumber)


if __name__ == "__main__":
    file = CreateRegister()

print("=========================================\n")
print("  Wainganga College Of engineering  \n")
print("=========================================\n")

print("Choose your Action\n")
print("1.	Add new Student")
print("2.	Delete Student")
print("3. 	Search Student")

choice = int(input("Your input please :"))
print("User have selected: userChoice={}".format(choice))
if(choice == 1):
    Add(file)
    print("New Student is added")

elif(choice == 2):
    name = input("Enter Name of Student:- ")
    print("Delete Student")
elif(choice == 3):
    name = input("Enter Name of Student:- ")
    print("It should display student Name",name)

else:
    print("Invalid Choice")