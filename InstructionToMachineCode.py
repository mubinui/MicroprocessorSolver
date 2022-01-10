# Instruction to machine code conversion input section
#MOV AX, BX
opcode_Name = 'MOV'
# Source = 0
# Destination =1
d_field = 1
register_Name = 'AX'
mod_reg_name = 'BX'
# Memory with no displacement = 00
# Memory with 8 displacement = 01
# Memory with 16 bit displacement = 10
# Both are register = 11
MOD_code = 11
# if displacement exists like 8B43 lb 43 hb 8b
Byte04 = '8b'
Byte03 = '43'
# if no displacement flag =0;  displacement flag = 1
flag = 0

# Register Chart
sixteen_bit_regs = ['AX', 'CX', 'DX', 'BX', 'SP', 'BP', 'SI', 'DI']
Eight_bit_regs = ['AL', 'CL', 'DL', 'BL', 'AH', 'CH', 'DH', 'BH']
mod_00 = ['[BX]+[SI]', '[BX]+[DI]', '[BP]+[SI]', '[BP]+[DI]', '[SI]', '[DI]', '[d16]', '[BX]']
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
if opcode_Name.__eq__('MOV'):
    print('100010', end='  ')

print(d_field, end=' ')

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

    if str2.__eq__(register_Name):
        print('0', end=' ')
        if MOD_code == 0 or MOD_code == 1:
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
