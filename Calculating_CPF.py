class CPF:
    '''Clase para validação de CPF'''

    def __init__(self, cpf='00000000000'):
        """
        Inicializa uma instância da classe CPF.

        Args:
            cpf (str): O CPF a ser validado, representado como uma string de 11 dígitos numéricos.
        """

        self._cpf = cpf
        self._sum1 = list(range(10, 1, -1))
        self._sum2 = list(range(11, 1, -1))
        self._cpf_valido = self._valida_cpf()

    def _primeiro_digito(self):
        """
        Calcula o primeiro dígito verificador do CPF.

        Returns:
            int: O primeiro dígito verificador.
        """

        dig1 = sum([(int(n) * s) for n, s in zip(self._cpf, self._sum1)]) % 11
        return 0 if dig1 < 2 else 11 - dig1

    def _segundo_digito(self):
        """
        Calcula o segundo dígito verificador do CPF.

        Returns:
            int: O primeiro dígito verificador.
        """
        dig2 = sum([(int(n) * s) for n, s in zip(self._cpf, self._sum2)]) % 11
        return 0 if dig2 < 2 else 11 - dig2

    def _valida_cpf(self):
        """
        Valida se o CPF fornecido é válido.

        Returns:
            bool: True se o CPF é válido, False caso contrário.
        
        Raises:
            ValueError: Se o CPF não possuir 11 dígitos numéricos.
        """

        if len(self._cpf) == 11 and self._cpf.isnumeric():
            digitos1 = list(self._cpf[-2:])
            dig1 = self._primeiro_digito()
            dig2 = self._segundo_digito()
            digitos2 = [str(dig1), str(dig2)]

            return digitos2 == digitos1

        raise ValueError('Seu CPF deve conter 11 digitos')

    def cpf_valido(self):
        """
        Verifica se o CPF fornecido é válido.

        Returns:
            bool: True se o CPF é válido, False caso contrário.
        """
        
        return self._cpf_valido


#Exemplo de uso:
'''cpf = CPF('11122233344')  # Digite o CPF aqui
if cpf.cpf_valido():
    print("CPF válido")
else:
    print("CPF inválido")'''
