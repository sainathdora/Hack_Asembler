import re

def Preprocess(filename): #filename.asm
    with open(f'{filename}.asm') as f:
        lines = [line.rstrip() for line in f]
        lines = [line.lstrip() for line in lines]
        lines = list(filter(lambda x:x!='', lines))
        # this list contains no white space, all we have to do now is worry about comments
        # <content-1> // <content-2>
        # select only content-1
        l2=[]
        for indx, ele in enumerate(lines):
            if(ele=="\n"):
                continue
            if(len(ele.split("//"))==1):
                l2.append(ele)
                continue
            left, right = ele.split("//")
            if(left!=""):
                left = left.rstrip()
                l2.append(left)
        lines=l2
        writetofile(lines, filename, 'asm')
    
    
def writetofile(lines, output, extension):
    # lines is list of line, output is where to write this parsed output generally .asm
    with open(f"{output}.{extension}", "w") as f:
        print(f"writing to {output}.{extension}")
        for indx, line in enumerate(lines):
            line = line.rstrip()
            line = line.lstrip()
            print(f"writing {line}")
            if(indx==len(lines)-1):
                f.write(line)
            else:
                f.write(line + "\n")

def Deal_A_Instruction(line):
    #assume A-Instruction
    res = "0"
    num = line[1:]
    # num = (<integer>) base-10
    num = format(int(num), '015b')
    res = res+num
    print(f"len = {len(res)}")
    return res
    # num is now in binary

def Parse(filename):
    Preprocess(filename)
    lines=[]
    with open(f'{filename}.asm', 'r') as f:
        lines = [line for line in f]
        for ind, line in enumerate(lines):
            if(line[0]=='@'):
                BinaryOp = Deal_A_Instruction(line)
                lines[ind]=BinaryOp
    print(lines)
    writetofile(lines, f'{filename}', 'hack')


def Preprocess_c_instruction(line):
    p2=line
    try:
        dest, p2 = line.split("=")
    except ValueError as e:
        line = "="+line
        dest, p2 = line.split("=")
    try:
        comp, jump = p2.split(";")
    except ValueError as e:
        line = line+";"
    return line
        

def Deal_with_C_instruction(line):
    line = Preprocess_c_instruction(line)
    dest, p2 = line.split("=")
    comp, jump = p2.split(";")
    
    # jump is string of length 0, if p2 = "D+1;"(eg)
    # identify the destination eg: dest -> (binary)
    dest_bits = find_destination_bits(dest)
    


def find_destination_bits(des):
    d = {
        "":"000",
        "M":"001",
        "D":"010",
        "MD":"011",
        "A":"100",
        "AM":"101",
        "AD":"110",
        "AMD":"111"
    }
    return d[dest]