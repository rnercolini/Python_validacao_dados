# Verifica se o sexo da pessoal foi digitado corretamente.
sexo = str(input('\033[34mDigite o sexo da pessoa [M/F]: \033[m')).upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('\033[31mDigite uma opção de sexo válida\033[m \033[32m[M/F]\033[m: ')).upper()
print('Fim')
