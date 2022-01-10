opcode = "10010" # 6 digit
d = 0  # 1 digit destination = 1
w = 0  # 1 digit
mod = 10  # 2 digit
reg = 100  # 3 digit
r_m = 100  # 3 digit
byte_three = 0 # 8 digit
byte_four = 0  # 8 digit
byte_five = 0  # 8 digit
byte_six = 0   # 8 digit

sixteen_bit_regs = ['AX', 'CX', 'DX', 'BX', 'SP','BP', 'SI','DI']
Eight_bit_regs = ['AL', 'CL', 'DL','BL', 'AH', 'CH', 'DH', 'BH']
mod_00 = ['[BX]+[SI]', '[BX]+[DI]','[BP]+[SI]', '[BP]+[DI]','[SI]', '[DI]','[D16(direct Addressing)]','[BX]']
mod_01 = ['[BX]+[SI]+d8', '[BX]+[DI]+d8','[BP]+[SI]+d8', '[BP]+[DI]+d8','[SI]+d8', '[DI]+d8','[BP]+d8','[BX]+d8']
mod_10 = ['[BX]+[SI]+d16', '[BX]+[DI]+d16','[BP]+[SI]+d16', '[BP]+[DI]+d16','[SI]+d16', '[DI]+d16','[BP]+d16','[BX]+d16']
RM = ['000', '001', '010', '011', '100', '101', '110', '111' ]

# Register Chart
sixteen_bit_regs = ['AX', 'CX', 'DX', 'BX', 'SP', 'BP', 'SI', 'DI']
Eight_bit_regs = ['AL', 'CL', 'DL', 'BL', 'AH', 'CH', 'DH', 'BH']
mod_00 = ['[BX]+[SI]', '[BX]+[DI]', '[BP]+[SI]', '[BP]+[DI]', '[SI]', '[DI]', '[D16(direct Addressing)]', '[BX]']
mod_01 = ['[BX]+[SI]+d8', '[BX]+[DI]+d8', '[BP]+[SI]+d8', '[BP]+[DI]+d8', '[SI]+d8', '[DI]+d8', '[BP]+d8', '[BX]+d8']
mod_10 = ['[BX]+[SI]+d16', '[BX]+[DI]+d16', '[BP]+[SI]+d16', '[BP]+[DI]+d16', '[SI]+d16', '[DI]+d16', '[BP]+d16',
          '[BX]+d16']
RM = ['000', '001', '010', '011', '100', '101', '110', '111']


# decimal to binary converter
def decimalToBinary(n):
    return bin(n).replace("0b", "")


# binary to hexa Converter
def HexadecimalToBinary(n):
    print(str("{0:08b}".format(int(n, 16))), end=' ')


# Instruction to machine code conversion
if opcode.__eq__('100010'):
    print('MOV', end='  ')



for i in range(len(sixteen_bit_regs)):
    str1 = str(sixteen_bit_regs[i])
    str2 = str(Eight_bit_regs[i])

    if str1.__eq__(register_Name):
        print('1', end=' ')
        if MOD_code == 0 or MOD_code == 1:
            print('0' + str(MOD_code), end=' ')
        else:
            print(MOD_code, end=' ')

        print(RM[i], end=' ')
        break

    if str2.__eq__(reg):
        print('0', end=' ')
        if mod == 0 or mod == 1:
            print('0' + str(MOD_code), end=' ')
        else:
            print(MOD_code, end=' ')
        print(RM[i], end=' ')
        break

if MOD_code == 00:
    for i in range(len(sixteen_bit_regs)):
        str1 = str(mod_00[i])

        if str1.__eq__(mod_reg_name):
            print(RM[i], end=' ')
            break

if MOD_code == 1:
    for i in range(len(sixteen_bit_regs)):
        str1 = str(mod_01[i])

        if str1.__eq__(mod_reg_name):
            print(RM[i], end=' ')
            break

if MOD_code == 10:
    for i in range(len(sixteen_bit_regs)):
        str1 = str(mod_10[i])

        if str1.__eq__(mod_reg_name):
            print(RM[i], end=' ')
            break

if MOD_code == 11:
    for i in range(len(sixteen_bit_regs)):
        str1 = str(sixteen_bit_regs[i])
        str2 = str(Eight_bit_regs[i])

        if str1.__eq__(mod_reg_name):
            print(RM[i], end=' ')
            break
        if str2.__eq__(mod_reg_name):
            print(RM[i], end=' ')
            break

if MOD_code > 1 and flag == 1:
    HexadecimalToBinary(Byte03)

    HexadecimalToBinary(Byte04)


elif flag == 1:
    HexadecimalToBinary(Byte03)
