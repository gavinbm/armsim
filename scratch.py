fin = open("input.txt").read().strip('\n')
fin = fin.splitlines()

Parsed = {"ins":"default",
          "dest":"default",
          "op1":"default",
          "op2":"default",}

def parse(line):
    parsed = line.split(" ")
    for i in range(0, len(parsed)):
        parsed[i]  = parsed[i].replace(" ", "").replace(",", "")
    return parsed

test = "add x1, x1, x0"
test2 = "mov x1, 3"
test3 = "mov x2, x1"
print(parse(test))
print(parse(test2))
print(parse(test3))
    