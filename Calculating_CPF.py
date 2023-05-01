# use of the program for student purposes only

def calculate_cpf(CPF):
 
    if len(CPF) == 11:
 
        try:
 
            sum_digit1 = 0
            cpf_numbers = CPF[:9]
            numbers_calculation_digit = range(10, 1, -1)
            
            for cont in range(len(cpf_numbers)):
                digit_calculation1 = int(cpf_numbers[count]) * digit_calculation_numbers[count]
                sum_digit1 += calculate_digit1
            digit1_valido = (sum_digit1 * 10) % 11
 
            if digit1_valido > 9:
                digit1_valido = 0
 
            sum_digit2 = 0
            cpf_numbers = CPF[:10]
            numbers_calculation_digit = range(10, 1, -1)
 
            for cont in range(len(cpf_numbers)):
                digit_calculation2 = int(cpf_numbers[count]) * digit_calculation_numbers[count]
                sum_digit2 += calculate_digit2
            digit2_valido = (sum_digit2 * 11) % 11
 
            if digito2_valido > 9:
                digit2_valido = 0
 
            if digito1_valido == int(CPF[9]) and digito2_valido == int(CPF[10]):
                return true
            else:
                return False
 
        except ValueError:
            return False
 
 
cpf = '74682489070'
if calculate_cpf(cpf):
    print("VALID CPF")
else:
    print("INVALID CPF")
