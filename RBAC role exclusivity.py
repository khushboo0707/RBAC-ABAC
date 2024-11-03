print("Input mutually exclusive roles in pairs, e.g. (a,b).")
print("To stop the input, enter duplicate roles, e.g. (a,a).")

file_role = open('Files/Role Info.txt', 'r')
file_RE = open('Files/Role Exclusivity.txt', 'w+')
content = file_role.read()
i = 0
while (i == 0):
    role1, role2 = input("\nEnter the pair for mutually exclusive roles: ").split()
    print("{} {}".format(role1, role2))
    if (role1 in content) & (role2 in content):
        if (role1 == role2):
            i = 1
        else:
            List1 = []
            List2 = []
            List1.append(role1)
            List2.append(role2)
            j = 0
            while ((j < len(List1)) or (j < len(List2))):
                file_RH = open('Files/Role Hierarchy.txt', 'r')
                for line in file_RH:
                    word = line.split()
                    if (word[0] in List1) and (List1.count(word[1]) == 0): 
                        List1.append(word[1])
                    if (word[0] in List2) and (List2.count(word[1]) == 0): 
                        List2.append(word[1])
                j += 1
                file_RH.close()
            if (role2 in List1) or (role1 in List2):
                print("Role exclusivity cannot be established as role hierarchy present.")
            else:
                file_RE.write(" ".join([role1, role2]) + '\n')
    else:
        print("Invalid role number entered.")

file_role.close()
file_RE.close()