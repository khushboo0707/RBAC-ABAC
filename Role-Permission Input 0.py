print("Input role-permission combinations in ordered pairs, e.g. (R, P).")
print("To stop the input, enter (R99, P99).")

file_role = open('Files/Role Info.txt', 'r')
file_per = open('Files/Permission Info.txt', 'r')

contentP = file_per.read()
contentR = file_role.read()
SmaxRP = "MaxRP:"
SmaxPR = "MaxPR:"
i = 0

while i == 0:
    role, per = input("\nEnter the ordered pair for role-permission combination: ").split()
    j = 0
    countR = 0
    countP = 0
    if per in contentP and role in contentR:
        file1 = open('Files/Role to Permission Assgn.txt', 'r')
        line = file1.readline()
        while j == 0: 
            if role in line: 
                for w in line.split():
                    if w != role and w != ':':
                        countR += 1
                    if w == per:
                        print("Role-permission combination already present.")
                        j = 1
                        countP += 1
                        break
            elif SmaxRP in line:
                for w in line.split(): 
                    if w != SmaxRP:
                        maxRP = int(w)
            elif SmaxPR in line:
                for w in line.split():
                    if w != SmaxPR:
                        maxPR = int(w)
            else:
                for w in line.split():
                    if w == per: 
                        countP += 1
            line = file1.readline()
            if not line:
                break
        file1.close()
        if j == 0:
            if countR < maxPR:
                if countP < maxRP:
                    offset = 5 + 3 * countR
                    file2 = open('Files/Role to Permission Assgn.txt', 'r')
                    for line in file2:
                        if role in line:
                            break
                        else:
                            offset += len(line)
                    file2.seek(0)
                    content = file2.read()
                    file2.close()
                    content = content[:offset] + per + " " + content[offset:]
                    file2 = open('Files/Role to Permission Assgn.txt', 'w')
                    file2.write(content)
                    print("Role-permission combination added.")
                    file2.close()
                else:
                    print("Permission has been assigned to max. no of roles, thus, role-permission combination not added.")
            else:
                print("Role has been assigned max. no of permissions, thus, role-permission combination not added.")
    else:
        if per == "P99" and role == "R99":
            i = 1
        else: 
            print("Invalid user or role ID entered.")

file_per.close()
file_role.close()