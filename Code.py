import Symbol_Table
def deal_with_A_instruction(line):
    # @value
    # here value is value is integer
    res = "0"
    num = line[1:]
    # num = (<integer>) base-10
    num = format(int(num), '015b')
    res = res+num
    return res

def deal_with_C_Instruction(dest, comp, jump):
    # clean c instruction dest=comp;jmp
    binary_ins = "111"
    

