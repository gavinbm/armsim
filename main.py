from reg import *

# Read input.txt in as list of strings
fin = open("input.txt").read().strip('\n')
fin = fin.splitlines()

# iterate, translate, and execute each line of code
# from input.txt
#print("Before interpretation\n")
print(Reg)
i = 0
while i < len(fin):
    line = fin[i]
    parsed = parse(line)
    print(parsed)
    if ":" in parsed[0]:
        Labels.append(dict(label = parsed[0].replace(":", ""), lineNum = i))
        print(Labels)
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
            code = ins[2:4]
            dest = parsed[1]
            if code:
                if Flags[code] == True:
                    for label in Labels:
                        if label["label"] == dest:
                            i = label["lineNum"]
            else:
                for label in Labels:
                    if label["label"] == dest:
                        i = label["lineNum"]
    # iteration
    i += 1

#print("after\n")
print(Reg)