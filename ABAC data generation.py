import random

user = input("Enter the number of users: ")
print(user)
uAttr = input("Enter the number of user attributes: ")
print(uAttr)
uAttrVal = input("Enter the number of possible user attribute values: ")
print(uAttrVal)
obj = input("Enter the number of objects: ")
print(obj)
oAttr = input("Enter the number of object attributes: ")
print(oAttr)
oAttrVal = input("Enter the number of possible object attribute values: ")
print(oAttrVal)
op = input("Enter the number of possible actions/operations: ")
print(op)
rule = input("Enter the number of rules: ")
print(rule)

file_user = open('Files/Subject Info.txt', 'w+')
file_UA = open('Files/Subject Attribute Info.txt', 'w+')
file_UAV = open('Files/Subject Attribute Value Info.txt', 'w+')
file_UAA = open('Files/Subject Attribute Assgn.txt', 'w+')
file_obj = open('Files/Object Info.txt', 'w+')
file_OA = open('Files/Object Attribute Info.txt', 'w+')
file_OAV = open('Files/Object Attribute Value Info.txt', 'w+')
file_OAA = open('Files/Object Attribute Assgn.txt', 'w+')
file_rule = open('Files/Rule Info.txt', 'w+')
file_op = open('Files/Operation Info.txt', 'w+')

user = int(user)
uAttr = int(uAttr)
uAttrVal = int(uAttrVal)
obj = int(obj)
oAttr = int(oAttr)
oAttrVal = int(oAttrVal)
op = int(op)
rule = int(rule)

for i in range(uAttr):
    file_UA.write("UA" + str(i+1) + '\n')
    for x in range(uAttrVal):
        file_UAV.write("UA" + str(i+1) + ":UA" + str(i+1) + str(x+1) + " ")
    file_UAV.write("UA" + str(i+1) + ":*" +'\n')

file_UA.close()
file_UAV.close()

for i in range(user):
    file_user.write("U" + str(i+1) + '\n')
    file_UAA.write("U" + str(i+1) + " : ")
    file_UAV = open('Files/Subject Attribute Value Info.txt', 'r')
    for line in file_UA:
        word = line.split()
        val = random.randint(1, uAttrVal)
        file_UAA.write(word[val-1] + " ")
    file_UAV.close()
    file_UAA.write('\n')

file_user.close()
file_UAA.close()

for i in range(oAttr):
    file_OA.write("OA" + str(i+1) + '\n')
    for x in range(oAttrVal):
        file_OAV.write("OA" + str(i+1) + ":OA" + str(i+1) + str(x+1) + " ")
    file_OAV.write("OA" + str(i+1) + ":*" +'\n')

file_OA.close()
file_OAV.close()

for i in range(obj):
    file_obj.write("O" + str(i+1) + '\n')
    file_OAA.write("O" + str(i+1) + " : ")
    file_OAV = open('Files/Object Attribute Value Info.txt', 'r')
    for line in file_OA:
        word = line.split()
        val = random.randint(1, oAttrVal)
        file_OAA.write(word[val-1] + " ")
    file_OAV.close()
    file_OAA.write('\n')

file_obj.close()
file_OAA.close()

for i in range(op):
    file_op.write("A" + str(i+1) + '\n')

file_op.close()

for i in range(rule):
    file_rule.write("R" + str(i+1) + " : ")
    file_UAV = open('Files/Subject Attribute Value Info.txt', 'r')
    for lineU in file_UAV:
        wordU = lineU.split()
        val = random.randint(1, uAttrVal+1)
        file_rule.write(wordU[val-1] + " ")
    file_OAV = open('Files/Object Attribute Value Info.txt', 'r')
    for lineO in file_OAV:
        wordO = lineO.split()
        val = random.randint(1, oAttrVal+1)
        file_rule.write(wordO[val-1] + " ")
    aVal = random.randint(1, op)
    file_rule.write("A" + str(aVal) + '\n')
    file_UAV.close()
    file_OAV.close()

file_rule.close()