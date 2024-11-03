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
    List = []
    ListP = []
    if (per in contentP) and (role in contentR):
        file = open('Files/Role to Permission Assgn.txt', 'r')
        line = file.readline()
        while j == 0:
            w = line.split() 
            if role in line:
                countR  += (len(w) - 2)
                if per in line:
                    print("Role-permission combination already present.")
                    j = 1
                    break
            elif SmaxRP in line:
                maxRP = int(w[1])
            elif SmaxPR in line:
                maxPR = int(w[1])
            else:
                if per in line: 
                    countP += 1
            line = file.readline()
            if not line:
                break
        file.close()
        if j == 0:
            file_RE = open('Files/Role Exclusivity.txt', 'r')
            List.append(role)
            for line in file_RE:
                word = line.split()
                if (word[0] == role) and (List.count(word[1]) == 0): 
                    List.append(word[1])
                if (word[1] == role) and (List.count(word[0]) == 0):
                    List.append(word[0])
            List.remove(role)
            file = open('Files/Role to Permission Assgn.txt', 'r')
            for line in file:
                for item in List:
                    if item in line:
                        for word in line.split():
                            if word != item and word != ':':
                                ListP.append(word)
            if per in ListP:
                print("Permission cannot be assigned to role as its mutually exclusive role has this permission.")
            else:
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
            file_RE.close()
    else:
        if per == "P99" and role == "R99":
            i = 1
        else: 
            print("Invalid user or role ID entered.")

file_per.close()
file_role.close()