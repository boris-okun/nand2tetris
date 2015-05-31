import string
import sys
import re

COMP = {
    '0'     : '101010',
    '1'     : '111111',
    '-1'    : '111010',
    'D'     : '001100',
    'A'     : '110000',
    '!D'    : '001101',
    '!A'    : '110001',
    '-D'    : '001111',
    '-A'    : '110011',
    'D+1'   : '011111',
    'A+1'   : '110111',
    'D-1'   : '001110',
    'A-1'   : '110010',
    'D+A'   : '000010',
    'D-A'   : '010011',
    'A-D'   : '000111',
    'D&A'   : '000000',
    'D|A'   : '010101' 
}

COMPA = {
    'M'     : '110000',
    '!M'    : '110001',
    '-M'    : '110011',
    'M+1'   : '110111',
    'M-1'   : '110010',
    'D+M'   : '000010',
    'D-M'   : '010011',
    'M-D'   : '000111',
    'D&M'   : '000000',
    'D|M'   : '010101'
}

DEST = {
    'null'  : '000',
    'M'     : '001',
    'D'     : '010',
    'MD'    : '011',
    'A'     : '100',
    'AM'    : '101',
    'AD'    : '110',
    'AMD'   : '111'
}

JUMP = {
    'null'  : '000',
    'JGT'   : '001',
    'JEQ'   : '010',
    'JGE'   : '011',
    'JLT'   : '100',
    'JNE'   : '101',
    'JLE'   : '110',
    'JMP'   : '111'
}

SYS_VARIABLES = {
    'R0'    : 0,
    'R1'    : 1,
    'R2'    : 2,
    'R3'    : 3,
    'R4'    : 4,
    'R5'    : 5,
    'R6'    : 6,
    'R7'    : 7,
    'R8'    : 8,
    'R9'    : 9,
    'R10'   : 10,
    'R11'   : 11,
    'R12'   : 12,
    'R13'   : 13,
    'R14'   : 14,
    'R15'   : 15,
    'SCREEN': 16384, 
    'KBD'   : 24576,
    'SP'    : 0,
    'LCL'   : 1,
    'ARG'   : 2,
    'THIS'  : 3,
    'THAT'  : 4
}

def GetCommand(line) :
    command = line.strip()
    command = ''.join(command.split(' '))
    if '//' in command :
        command = command.rsplit('//', 1)[0]
    return command

def ParseLabels(lines):
    counter = 0
    lables = {}
    for line in lines :
        command = GetCommand(line)
        if command.startswith('(') :
            lable = command[1:-1]
            if lable in lables :
                raise Exception("Duplicated label")
            lables[lable] = counter
        elif len(command) > 0 :
            counter += 1
    return lables

def ParseCommand(comm) :
    if '=' in comm :
        (dest, comp) = comm.split('=')
    else :
        dest = 'null'
        comp = comm
    binaryCommand = ''
    if comp in COMP :
        binaryCommand = '0' + COMP[comp]
    elif comp in COMPA :
        binaryCommand = '1' + COMPA[comp]
    else :
        raise Exception("Unknown comp command: " + comp)
    if dest in DEST :
        binaryCommand += DEST[dest]
    else :
        raise Exception("Unknown destination: " + dest)
    return binaryCommand

def ParseJump(jump) :
    if jump in JUMP :
        return JUMP[jump]
    else :
        raise Exception("Unknown jump: " + jump)

def ParseProgram(lines, lables) :            
    variables = SYS_VARIABLES
    varAdress = 16
    for line in lines :
        command = GetCommand(line)
        if len(command) == 0 or command.startswith('(') :
            continue
        if command.startswith('@') :
            var = command[1:]
            if var.isdigit() :
                address = int(var)
            elif var in lables :
                address = lables[var]
            elif var in variables :
                address = variables[var]
            else :
                address = varAdress
                variables[var] = varAdress
                varAdress += 1
            binaryCommand = '0' + bin(address)[2:].zfill(15)
        else :  
            if ';' in command :
                (comm, jump) = command.split(';')
            else :
                comm = command
                jump = 'null'
            binaryCommand = '111' + ParseCommand(comm) + ParseJump(jump)
        print binaryCommand
                

input = sys.argv[1]
lines = open(input, 'rb').readlines()
lables = ParseLabels(lines)
ParseProgram(lines, lables)

        
