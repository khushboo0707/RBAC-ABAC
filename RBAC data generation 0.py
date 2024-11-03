import random

user = input("Enter the number of users: ")
print(user)
role = input("Enter the number of roles: ")
print(role)
per = input("Enter the number of permissions: ")
print(per)
maxR = input("Enter the max no. of roles assigned to a user (<=" + role + "): ")
print(maxR)
maxP = input("Enter the max no. of permissions assigned to a role (<=" + per + "): ")
print(maxP)

user = int(user)
role = int(role)
per = int(per)
maxR = int(maxR)
maxP = int(maxP)

file_user = open('Files/User Info.txt', 'w+')
file_role = open('Files/Role Info.txt', 'w+')
file_per = open('Files/Permission Info.txt', 'w+')
file_URA = open('Files/User to Role Assgn.txt', 'w+')
file_RPA = open('Files/Role to Permission Assgn.txt', 'w+')

for i in range(1, user+1):
    file_user.write("U" + str(i) + '\n')
    j = random.randint(1, maxR)
    List = []
    while (len(List) != j):
        r = random.randint(1, role)
        if r not in List:
            List.append(r)
    List.sort()
    file_URA.write("U" + str(i) + " : ")
    for k in List:
        file_URA.write("R" + str(k) + " ")
    file_URA.write('\n')

for i in range(1, role+1):
    file_role.write("R" + str(i) + '\n')
    j = random.randint(1, maxP)
    List = []
    while (len(List) != j):
        r = random.randint(1, per)
        if r not in List:
            List.append(r)
    List.sort()
    file_RPA.write("R" + str(i) + " : ")
    for k in List:
        file_RPA.write("P" + str(k) + " ")
    file_RPA.write('\n')

for i in range(1, per+1):
    file_per.write("P" + str(i) + '\n')

file_user.close()
file_role.close()
file_per.close()
file_URA.close()
file_RPA.close()