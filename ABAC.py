user, obj, action = input("Enter the User ID, Object ID and Action ID: ").split()
print(user)
print(obj)
print(action)

file_user = open('Files/Subject Info.txt', 'r')
file_obj = open('Files/Object Info.txt', 'r')
file_op = open('Files/Operation Info.txt', 'r')

contentU = file_user.read()
contentO = file_obj.read()
contentA = file_op.read()
i = 0
while (i == 0):
    if user in contentU: 
        if obj in contentO:
            if action in contentA:
                i = 1
                print("Valid Input")
            else:
                print("Invalid Action ID")
        else:
            print("Invalid Object ID")
    else:
        print("Invalid User ID")
    
    if (i == 0):
        user, obj, action = input("Enter the User ID, Object ID and Action ID: ").split()
        print(user)
        print(obj)
        print(action)

file_UAA = open('Files/Subject Attribute Assgn.txt', 'r')
lineUAA = file_UAA.readline()
i = 0
ListU = [] 
while (i == 0):
    if user in lineUAA:
        i = 1
        for wordU in lineUAA.split():
            if ((wordU != user) & (wordU != ':')):
                ListU.append(wordU)
    else:
        lineUAA = file_UAA.readline()

print("Attributes of the user: ")
print(ListU)

file_OAA = open('Files/Object Attribute Assgn.txt', 'r')
lineOAA = file_OAA.readline()
i = 0
ListO = []
while (i == 0):
    if obj in lineOAA:
        i = 1
        for wordO in lineOAA.split():
            if ((wordO != obj) & (wordO != ':')):
                ListO.append(wordO)
    else:
        lineOAA = file_OAA.readline()

print("Attributes of the user: ")
print(ListO)

List = ListU + ListO
List.append(action)
file_rule = open("Files/Rule Info.txt", 'r')
i = 0
line = file_rule.readline()
l = len(List)
while (i == 0):
    j = 0
    k = 0
    word = line.split()
    for j in range(l):
        if word[j+2][-1] != '*':
            if word[j+2] != List[j]:
                k = 1
                break
    if k == 0:
        i = 1
        break
    line = file_rule.readline()
    if not line:
        break

if (i == 1):
    print("User allowed to operate on object requested.")
else:
    print("User not allowed to operate on object requested.")

file_user.close()  
file_UAA.close()
file_obj.close()
file_OAA.close()
file_op.close()
file_rule.close()
