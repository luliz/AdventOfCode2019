import math

with open ("input1.txt", "r") as file:
    raw=file.readline()
    opcode=raw.split(',')
    for i in range(len(opcode)):
        opcode[i]=int(opcode[i])
    opcode[1]=12
    opcode[2]=2
    for i in range(math.floor(len(opcode)/4)):
        if (opcode[4*i]==1):
            opcode[opcode[4*i+3]]=opcode[opcode[4*i+1]]+opcode[opcode[4*i+2]]
        elif (opcode[4*i]==2):
            opcode[opcode[4*i+3]]=opcode[opcode[4*i+1]]*opcode[opcode[4*i+2]]
        elif (opcode[4*i]==99):
            break
        else:
            print ("Unknown operation.")
            break
    print (opcode)
