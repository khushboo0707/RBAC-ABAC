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
    j = 0
    countR = 0
    countU = 0
    if user in contentU and role in contentR:
        file1 = open('Files/User to Role Assgn.txt', 'r')
        line = file1.readline()
        while j == 0: 
            if user in line: 
                for w in line.split():
                    if w != user and w != ':':
                        countU += 1
                    if w == role:
                        print("User-role combination already present.")
                        j = 1
                        countR += 1
                        break
            elif SmaxRU in line:
                for w in line.split(): 
                    if w != SmaxRU:
                        maxRU = int(w)
            elif SmaxUR in line:
                for w in line.split():
                    if w != SmaxUR:
                        maxUR = int(w)
            else:
                for w in line.split():
                    if w == role: 
                        countR += 1
            line = file1.readline()
            if not line:
                break
        file1.close()
        if j == 0:
            if countU < maxRU:
                if countR < maxRU:
                    offset = 5 + 3 * countU
                    file2 = open('Files/User to Role Assgn.txt', 'r')
                    for line in file2:
                        if user in line:
                            break
                        else:
                            offset += len(line)
                    file2.seek(0)
                    content = file2.read()
                    file2.close()
                    content = content[:offset] + role + " " + content[offset:]
                    file2 = open('Files/User to Role Assgn.txt', 'w')
                    file2.write(content)
                    print("User-role combination added.")
                    file2.close()
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