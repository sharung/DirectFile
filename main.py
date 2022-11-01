# with open("my_file.txt", "r") as file1:
#     # i = 0
#     # for text in file1:
#     #     print(f"baris ke {i} : ", text)
#     #     i += 1
#
#     file_list = file1.readlines()
#     print(file_list[1])


"""write file"""
# file1 = "coba_text.txt"
# with open(file1, "w") as file_test:
#     file_test.write("This is first line\n")
#     file_test.write("This is second line")
#
# with open(file1, "r") as read_test:
#     print(read_test.read())

""" Create new file with value of list """
# new_lines = ["this is the firs\n", "this is the second\n", "this is the last"]
#
# with open("test_list.txt", "w") as new_file:
#     # looping the index of new_lines
#     for line in new_lines:
#         print(line)
#         new_file.write(line)
#
# with open("test_list.txt", "r") as read_file:
#     print(read_file.read())

""" menambahkan kalimat tampa mengganti yang sudah ada 
    Append the text """
# with open("test_list.txt", "a") as add_text:
#     add_text.write("tambahan 1\n")
#     add_text.write("tambahan 2\n")
#     add_text.write("tambahan 3\n")
#
# with open("test_list.txt", "r") as read_file:
#     print(read_file.read())

""" Additional Write """
# r+ : Read and Write
# w+ : Write and Read
# a+ : Appending and Read

# with open("test1.txt", "a+") as file1:
#     print("Initial location : {} ".format(file1.tell()))
#
#     data = file1.read()
#     if (not data):
#         print("read nothing")
#     else:
#         print(data)
#
#     file1.seek(0, 0) # go back to start
#
#     print("\nInital location : {}".format(file1.tell()))
#     data = file1.read()
#     if (not data):
#         print("read nothing")
#     else:
#         print(data)
#
#     print("Location after read : {} ".format(file1.tell()))


""" Exercise """
from random import randint as rnd

memReg = "members.txt"
exReg = "inactive.txt"
fee = ("yes", "no")


def genFiles(current, old):

    with open(current, 'w+') as writefile:
        writefile.write("Membership No Date Joined Active \n")
        data = "{:^13} {:<11} {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015, 2020)) + "-" + str(rnd(1, 12)) + "-" + str(rnd(1, 25))
            writefile.write(data.format(rnd(10000, 99999), date, fee[rnd(0, 1)]))

    with open(old, "w+") as writefile:
        writefile.write("Membership No Date Joined Active \n")
        data = "{:^13} {:<11} {:<6}\n"

        for rowno in range(3):
            date = str(rnd(2015, 2020)) + "-" + str(rnd(1, 12)) + "-" + str(rnd(1, 25))
            writefile.write(data.format(rnd(10000, 99999), date, fee[1]))


genFiles(memReg, exReg)


def cleanFiles(currentMem, exMem):

    with open(currentMem, "r+") as file1:
        with open(exMem, "a+") as file2:
            file1.seek(0)
            member_list = file1.readlines()
            header = member_list[0]
            member_list.pop(0)

            inactive = [member for member in member_list if ('no' in member)]
            file1.seek(0)
            file2.write(header)
            for member in member_list:
                if (member in inactive):
                    file2.write(member)
                else:
                    file1.write(member)

            file1.truncate()

memReg = 'members.txt'
exMem = 'inactive.txt'
cleanFiles(memReg, exMem)

# see file

header = "Membership No  Date Joined  Active  \n"

with open(memReg, 'r') as readFile:
    print("Active members: \n\n")
    print(readFile.read())

with open(exReg, 'r') as readFile:
    print("Inactive members: \n\n")
    print(readFile.read())