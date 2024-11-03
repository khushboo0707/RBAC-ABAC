print("Input user-role combinations in ordered pairs, e.g. (U,R).")
print("To stop the input, enter (U99, R99).")

file_user = open('Files/User Info.txt', 'r')
file_role = open('Files/Role Info.txt', 'r')

contentU = file_user.read()
contentR = file_role.read()
SmaxUR = "MaxUR:"
SmaxRU = "MaxRU:"

i = 0
while i == 0:
    user, role = input("\nEnter the ordered pair for user-role combination: ").split()
    List = []
    j = 0
    countR = 0
    countU = 0
    if (user in contentU) and (role in contentR):
        file = open('Files/User to Role Assgn.txt', 'r')
        line = file.readline()
        while j == 0: 
            if user in line: 
                for w in line.split():
                    if w != user and w != ':':
                        countU += 1
                        List.append(w)
                    if w == role:
                        print("User-role combination already present.")
                        j = 1
                        break
            elif SmaxRU in line:
                w = line.split() 
                maxRU = int(w[1])
            elif SmaxUR in line:
                w = line.split()
                maxUR = int(w[1])
            else:
                if role in line: 
                    countR += 1
            line = file.readline()
            if not line:
                break
        file.close()
        if j == 0:
            file_RE = open('Files/Role Exclusivity.txt', 'r')
            for line in file_RE:
                word = line.split()
                if (word[0] in List) and (List.count(word[1]) == 0): 
                    List.append(word[1])
            file_RE.close()
            if role in List:
                print("Role cannot be assigned to user as user has its mutually exclusive role.")
            else:
                if countU < maxRU:
                    if countR < maxRU:
                        offset = 5 + 3 * countU
                        file = open('Files/User to Role Assgn.txt', 'r')
                        for line in file:
                            if user in line:
                                break
                            else:
                                offset += len(line)
                        file.seek(0)
                        content = file.read()
                        file.close()
                        content = content[:offset] + role + " " + content[offset:]
                        file = open('Files/User to Role Assgn.txt', 'w')
                        file.write(content)
                        print("User-role combination added.")
                        file.close()
                    else:
                        print("Role has been assigned to max. no of users, thus, user-role combination not added.")
                else:
                    print("User has been assigned max. no of roles, thus, user-role combination not added.")
    else:
        if user == "U99" and role == "R99":
            i = 1
        else: 
            print("Invalid user or role ID entered.")

file_user.close()
file_role.close()