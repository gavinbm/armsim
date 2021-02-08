from reg import *

# Read input.txt in as list of strings
fin = open("input.txt").read().strip('\n')
fin = fin.splitlines()

print("Before\n")
print(Reg)

# Storing all labels and line numbers in input.txt
getLabels(fin)

# iterate, translate, and execute each line of code
# from input.txt
i = 0
while i < len(fin):
    parsed = parse(fin[i])
    ins = parsed[0]
    if "mov" in ins:
        dest = parsed[1]
        op1 = parsed[2]
        mov(dest, op1)
    elif "add" in ins:
        dest = parsed[1]
        op1 = parsed[2]
        op2 = parsed[3]
        add(dest, op1, op2)
    elif "sub" in ins:
        dest = parsed[1]
        op1 = parsed[2]
        op2 = parsed[3]
        sub(dest, op1, op2)
    elif "mul" in ins:
        dest = parsed[1]
        op1 = parsed[2]
        op2 = parsed[3]
        mul(dest, op1, op2)
    elif "cmp" in ins:
        dest = parsed[1]
        op1 = parsed[2]
        cmp(dest, op1)
    elif "b" in ins:
        if "cbz" in ins or "cbnz" in ins:
            dest = parsed[1]
            cmp(dest, "x8")
            if "cbz" in ins and Flags["eq"] == True:
                i = k
            elif "cbnz" in ins and Flags["eq"] == False:
                i = k
        else:
            if "b." in ins:
                flagCode = parsed[0][2:4]
                if Flags[flagCode]:
                    i = Labels[parsed[1]]
            else:
                i = Labels[parsed[1]]
                
    # iteration
    i += 1

print("\nafter\n")
print(Reg)