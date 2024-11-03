user = input("Enter the User ID: ")
print(user)

file_user = open('Files/User Info.txt', 'r')
contentU = file_user.read()
i = 0
while (i == 0):
    if user in contentU:
        i = 1
        print("Valid User ID")
    else:
        print("Invalid User ID")
        user = input("Enter the User ID: ")
        print(user)

file_URA = open('Files/User to Role Assgn.txt', 'r')
lineURA = file_URA.readline()
i = 0
ListR = [] 
while (i == 0):
    if user in lineURA:
        i = 1
        for word in lineURA.split():
            if ((word != user) & (word != ':')):
                ListR.append(word)
    else:
        lineURA = file_URA.readline()
print("Roles assigned to user: ")
print(ListR)

per = input("Enter the permission number to use: ")
print(per)

file_per = open('Permission Info.txt', 'r')
contentP = file_per.read()
i = 0
while (i == 0):
    if per in contentP:
        i = 1
        print("Valid Permission Number")
    else:
        print("Invalid Permission Number")
        per = input("Enter the permission number to use: ")
        print(per)

file_RPA = open('Files/Role to Permission Assgn.txt', 'r')
lineRPA = file_RPA.readline()
i = 0
l = len(ListR)
while (i == 0):
    j = 0
    for j in range(l):
        str = ListR[j]
        if str in lineRPA:
            if per in lineRPA:
                i = 1
                break
    lineRPA = file_RPA.readline()
    if not lineRPA:
        break

if (i == 1):
    print("User allowed to use permission requested.")
else:
    print("User not allowed to use permission requested.")

file_user.close()  
file_URA.close()
file_per.close()
file_RPA.close()