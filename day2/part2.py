import math

def generate_opcode(filename):
    with open (filename, "r") as file:
        raw=file.readline()
        opcode=raw.split(',')
        for i in range (len(opcode)):
            opcode[i]=int(opcode[i])
    return opcode

def calculate_opcode(opcode):
    for i in range(math.floor(len(opcode)/4)):
        if (opcode[4*i]==1):
            opcode[opcode[4*i+3]]=opcode[opcode[4*i+1]]+opcode[opcode[4*i+2]]
        elif (opcode[4*i]==2):
            opcode[opcode[4*i+3]]=opcode[opcode[4*i+1]]*opcode[opcode[4*i+2]]
        elif (opcode[4*i]==99):
            break
        else:
            return [0] 
    return opcode

for noun in range(100):
    for verb in range(100):
        opcode=generate_opcode('input1.txt')
        opcode[1]=noun
        opcode[2]=verb
        if (calculate_opcode(opcode)[0]==19690720):
            print (100*noun+verb)
