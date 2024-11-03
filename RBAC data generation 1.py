import random

user = input("Enter the number of users: ")
print(user)
role = input("Enter the number of roles: ")
print(role)
per = input("Enter the number of permissions: ")
print(per)
maxRU = input("Enter the max no. of roles assigned to a user (<=" + role + "): ")
print(maxRU)
maxPR = input("Enter the max no. of permissions assigned to a role (<=" + per + "): ")
print(maxPR)
maxUR = input("Enter the max no. of users assigned to a role (<=" + user + "): ")
print(maxUR)
maxRP = input("Enter the max no. of roles assigned to a permission (<=" + role + "): ")
print(maxRP)

file_user = open('Files/User Info.txt', 'w+')
file_role = open('Files/Role Info.txt', 'w+')
file_per = open('Files/Permission Info.txt', 'w+')
file_URA = open('Files/User to Role Assgn.txt', 'w+')
file_URA.write("MaxRU: " + maxRU + '\n')
file_URA.write("MaxUR: " + maxUR + '\n')
file_RPA = open('Files/Role to Permission Assgn.txt', 'w+')
file_RPA.write("MaxPR: " + maxPR + '\n')
file_RPA.write("MaxRP: " + maxRP + '\n')

user = int(user)
role = int(role)
per = int(per)
maxRU = int(maxRU)
maxPR = int(maxPR)
maxUR = int(maxUR)
maxRP = int(maxRP)

ListUR = []
for i in range(role):
    ListUR.append(0)

ListRP = []
for i in range(per):
    ListRP.append(0)

for i in range(user):
    file_user.write("U" + str(i+1) + '\n')
    file_URA.write("U" + str(i+1) + " : ")
    j = random.randint(1, maxRU)
    List = []
    ListNot = []
    r = random.randint(1, role)
    for x in range(j):
        while r in List or ListUR[r-1] >= maxUR:
            r = random.randint(1, role)
            if all(item == maxUR for item in ListUR):
                break
        List.append(r)
    List.sort()
    for x in List:
        ListUR[x-1] += 1
        file_URA.write("R" + str(x) + " ")
    file_URA.write('\n')

for i in range(role):
    file_role.write("R" + str(i+1) + '\n')
    file_RPA.write("R" + str(i+1) + " : ")
    j = random.randint(1, maxPR)
    List = []
    ListNot = []
    p = random.randint(1, per)
    for x in range(j):
        while p in List or ListRP[p-1] >= maxRP:
            p = random.randint(1, per)
            if all(item == maxRP for item in ListRP):
                break
        List.append(p)
    List.sort()
    for x in List:
        ListRP[x-1] += 1
        file_RPA.write("P" + str(x) + " ")
    file_RPA.write('\n')

for i in range(per):
    file_per.write("P" + str(i+1) + '\n')

file_user.close()
file_role.close()
file_per.close()
file_URA.close()
file_RPA.close()