import os

def createfile():
    file = open("studentinfo.txt", "a+")
    return file

def addtofile(file, studentid, studentname, age, phonenumber):
    file.write("{}/{}/{}/{}\n".format(studentid,studentname,age,phonenumber))
    file.close()

    def readfile():
        file = open("studeninfo.txt")
        print(file.read())
        file.close()


def checkthefile(f, studentname):
    f = open("studentinfo.txt", "r")
    data = f.readlines()
    data = " "
    for line in data :
        splitData = line.split("/")
        rollNum = splitData[0]
        studentname = splitData[1]
        age = splitData[2]
        phonenumber = splitData[3]
        if studentname == studentname:
            print("{}/{}/{}".format(rollNum, studentname, age, phonenumber))


    def checkifstudentexit(f, studentname) :
f = open("studentinfo.txt", "r")
data = " "
data = f.readlines()
for line in data:
    splitData = line.split("/")
    rollNum = splitData[0]
    studentname = splitData[1]
    age = splitData[2]
    phonenumber = splitData[3]
    if studentname == studentname:
        print("{}/{}/{}".format(rollNum, studentname, age, phonenumber))

def choice():
 print("********Student management system*******")
 print("1. add new student \n 2. delete student \n 3. search student \n 4. list student")
 choice = int(input("enter your choice : "))


def add(file):
    print("****Add student information**** ")
    f = open("Studentinfo.txt", "r")
    studentId = len(f.readlines()) + 1
    name = input("Enter Student Name = ")
    age = int(input("Enter Age = "))
    phoneNumber = int(input("Enter Phone Number = "))
    check = checkIfStudentExit(file, name)
    if check is True:
        print("student already exit ")
        return False
    else:
        addToFile(file, studentId, name, age, phoneNumber)


if _name_ == '_main_':
    f = createFile()
    ch = choice()
    if ch == 1:
        result = add(f)
        if result is False :
            pass
        else:
            print("\n")
            print("----New Student added-----")
            readFile()

    elif ch == 2:
        readFile()
        Name = input("Enter the Name You Want To Delete the data = ")

    elif ch == 3:
        Name = input("Enter the Name You Want To Search = ")
        checkTheFile(f, Name)
    elif ch == 4:
        readFile()
    elif ch == 5:
        updateStudentInfo()
    else:
        print("Enter A Valid Option")
