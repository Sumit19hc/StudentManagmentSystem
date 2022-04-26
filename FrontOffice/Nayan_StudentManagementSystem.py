import os


def createFile():
    file = open("Studentinfo.txt", "a+")
    return file


def addToFile(file, studentId, name, age, phoneNumber):
    file.write("{}|{}|{}|{}\n".format(studentId, name, age, phoneNumber))
    file.flush()
    file.seek(0)
    file.close()


def readFile():
    file = open("Studentinfo.txt")
    print(file.read())
    file.close()


def checkTheFile(f, studentname):
    f = open("Studentinfo.txt", "r")
    data = " "
    data = f.readlines()
    for line in data:
        splitData = line.split("|")
        rollNum = splitData[0]
        name = splitData[1]
        age = splitData[2]
        phoneNumber = splitData[3]
        if studentname == name:
            print("{}|{}|{}|{}".format(rollNum, name, age, phoneNumber))


def checkIfStudentExit(f, studentname):
    f = open("Studentinfo.txt", "r")
    data = " "
    data = f.readlines()
    for line in data:
        splitData = line.split("|")
        rollNum = splitData[0]
        name = splitData[1]
        age = splitData[2]
        phoneNumber = splitData[3]
        if studentname == name:
            print("\n{}|{}|{}|{}".format(rollNum, name, age, phoneNumber))
            return True


# def updateStudentInfo():
#     file_r = open("Studentinfo.txt", "r")
#     file_w = open("temp.txt", "w")
#     print(file_r.read())
#     rollNum = input("Enter The Roll Number   =  ")
#     s = " "
#     while s:
#         s = file_r.readline()
#         lis = s.split("|")
#         if len(s) > 0:
#             if lis[0] == rollNum:
#                 name = input("Enter Student Name = ")
#                 age = int(input("Enter Age = "))
#                 phoneNumber = int(input("Enter Phone Number = "))
#                 file_w.write(rollNum, name, age, phoneNumber)
#             else:
#                 file_w.write(s)
#     file_w.close()
#     file_r.close()
#     os.remove("Studentinfo.txt")
#     os.rename("temp.txt", "Studentinfo.txt")


def choice():
    print("******** Student Management System ********")
    print(
        ''' 1.Add New Student\n 2.Delete Student\n 3.Search Student \n 4.List Student \n 5.Update Student Information 
        \n''')
    choice = int(input("       Enter You choice :- "))
    return choice


def add(file):
    print("*********Add student information********* ")
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


if __name__ == '__main__':
    f = createFile()
    ch = choice()
    if ch == 1:
        result = add(f)
        if result is False:
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
        pass
        # updateStudentInfo()
    else:
        print("Enter A Valid Option")
