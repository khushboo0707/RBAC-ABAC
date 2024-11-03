print("Input role hierarchy in ordered pairs, e.g. (a,b) such that (a>b).")
print("To stop the input, enter duplicate roles, e.g. (a,a).")

file_role = open('Files/Role Info.txt', 'r')
file_RH = open('Files/Role Hierarchy.txt', 'w+')
content = file_role.read()
i = 0

while (i == 0):
    role1, role2 = input("\nEnter the ordered pair for role hierarchy: ").split()
    print("{} > {}".format(role1, role2))
    if (role1 in content) & (role2 in content):
        if (role1 == role2):
            i = 1
        else:
            List1 = []
            List2 = []
            List1.append(role1)
            List2.append(role2)
            file_RE = open('Files/Role Exclusivity.txt', 'r')
            for line in file_RE:
                word = line.split()
                if (word[0] == role1): 
                    List1.append(word[1])
                if (word[0] == role2):
                    List2.append(word[1])
            file_RE.close()
            if (role2 in List1) or (role1 in List2):
                print("Role hierarchy cannot be established as roles are mutually exclusive.")
            else:
                file_RH.write(" ".join([role1, role2]) + '\n')
    else:
        print("Invalid role number entered.")

file_role.close()
file_RH.close()